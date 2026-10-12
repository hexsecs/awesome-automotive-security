"""Tests for the pure logic of the discovery tooling.

Run with:  python3 -m unittest discover -s tests

Only the decision logic is tested: classifying a probe, vetting a URL against the
list's own data, and judging a GitHub record. Nothing here touches the network.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_candidate as cc  # noqa: E402
import probe_egress as pe  # noqa: E402
import validate_list as vl  # noqa: E402

NOW = datetime(2026, 10, 10, tzinfo=timezone.utc)

ENTRIES = [
    {"line": 37, "section": "CAN Bus Analysis", "name": "CANgaroo",
     "url": "https://github.com/Schildkroet/CANgaroo"},
    {"line": 105, "section": "RF and Key Fob Analysis", "name": "Universal Radio Hacker (URH)",
     "url": "https://github.com/jopohl/urh"},
]
DECISIONS = [
    {"name": "flipper-tesla-fsd", "url": "https://github.com/hypery11/flipper-tesla-fsd",
     "decision": "rejected", "reason": "tuning tool", "date": "2026-09-27", "ref": "#25"},
    {"name": "URH", "url": "https://github.com/jopohl/urh", "decision": "kept",
     "reason": "canonical", "date": "2026-09-23", "ref": "#21"},
]
LEADS = [{"name": "AutoHack", "url": "https://zenodo.org/records/20321379",
          "reason": "unverified", "date": "2026-10-10"}]
HOSTS = {
    "avoid": [{"host": "researchgate.net", "reason": "bot challenge"}],
    "excluded": [{"host": "dl.acm.org", "reason": "403"}],
    "reliable": [],
}


def vet(url: str) -> tuple[list[str], list[str]]:
    return cc.local_findings(url, ENTRIES, DECISIONS, LEADS, HOSTS)


class ClassifyTests(unittest.TestCase):
    def test_page_is_reachable(self):
        self.assertEqual(pe.classify(200, None)[0], "reachable")

    def test_bot_filter_is_refused_not_blocked(self):
        for status in (202, 403, 429, 503):
            self.assertEqual(pe.classify(status, None)[0], "refused", status)

    def test_missing_page_still_proves_the_host_answers(self):
        self.assertEqual(pe.classify(404, None)[0], "reachable")

    def test_refused_connect_is_the_proxy(self):
        self.assertEqual(pe.classify(None, "Tunnel connection failed: 403 Forbidden")[0], "blocked")

    def test_dns_failure(self):
        self.assertEqual(pe.classify(None, "[Errno -2] Name or service not known")[0], "dns")
        self.assertEqual(pe.classify(None, "getaddrinfo ENOTFOUND zenodo.org")[0], "dns")

    def test_anything_else_is_an_error(self):
        self.assertEqual(pe.classify(None, "timed out")[0], "error")


class LocalFindingTests(unittest.TestCase):
    def test_duplicate_url_blocks(self):
        blockers, _ = vet("https://github.com/Schildkroet/CANgaroo")
        self.assertTrue(any("already listed as 'CANgaroo'" in b for b in blockers))

    def test_duplicate_ignores_case_slash_and_git_suffix(self):
        blockers, _ = vet("https://github.com/schildkroet/cangaroo.git")
        self.assertTrue(blockers)
        blockers, _ = vet("https://github.com/Schildkroet/CANgaroo/")
        self.assertTrue(blockers)

    def test_rejected_decision_blocks_and_says_how_to_overturn(self):
        blockers, _ = vet("https://github.com/hypery11/flipper-tesla-fsd")
        self.assertEqual(len(blockers), 1)
        self.assertIn("rejected in #25", blockers[0])
        self.assertIn("delete its record", blockers[0])

    def test_kept_decision_warns_without_blocking_a_new_candidate(self):
        # The URH URL is also listed, so it blocks; the kept record still explains why.
        blockers, warnings = vet("https://github.com/jopohl/urh")
        self.assertTrue(blockers)
        self.assertTrue(any("kept" in w for w in warnings))

    def test_lead_is_a_warning(self):
        blockers, warnings = vet("https://zenodo.org/records/20321379")
        self.assertEqual(blockers, [])
        self.assertTrue(any("already a lead" in w for w in warnings))

    def test_avoid_host_blocks(self):
        blockers, _ = vet("https://www.researchgate.net/publication/1")
        self.assertTrue(any("avoid" in b for b in blockers))

    def test_excluded_host_warns_that_ci_cannot_verify(self):
        blockers, warnings = vet("https://dl.acm.org/doi/10.1145/1")
        self.assertEqual(blockers, [])
        self.assertTrue(any("excluded from link checking" in w for w in warnings))

    def test_same_name_other_url_asks_if_it_is_the_same_project(self):
        blockers, warnings = vet("https://github.com/wikilift/CANgaroo")
        self.assertEqual(blockers, [])
        self.assertTrue(any("same project under another URL" in w for w in warnings))

    def test_unknown_candidate_is_clear(self):
        self.assertEqual(vet("https://github.com/example/new-tool"), ([], []))


class RepoFindingTests(unittest.TestCase):
    base = {"full_name": "a/b", "stargazers_count": 40, "forks_count": 3,
            "license": {"spdx_id": "MIT"}, "pushed_at": "2026-09-01T00:00:00Z"}

    def judge(self, **over):
        return cc.repo_findings({**self.base, **over}, ("a", "b"), over.pop("_parent", None), NOW)

    def test_healthy_repo_has_no_warnings(self):
        facts, warnings = self.judge()
        self.assertEqual(warnings, [])
        self.assertTrue(any("40 stars" in f for f in facts))

    def test_archived(self):
        self.assertTrue(any("archived" in w for w in self.judge(archived=True)[1]))

    def test_dormant_after_two_years(self):
        self.assertTrue(any("dormant" in w for w in self.judge(pushed_at="2023-01-01T00:00:00Z")[1]))
        self.assertEqual(self.judge(pushed_at="2025-01-01T00:00:00Z")[1], [])

    def test_moved_repo(self):
        self.assertTrue(any("moved" in w for w in self.judge(full_name="c/d")[1]))

    def test_fork_of_a_far_more_starred_parent_is_called_out(self):
        data = {**self.base, "stargazers_count": 4, "fork": True, "parent": {"full_name": "up/stream"}}
        _, warnings = cc.repo_findings(data, ("a", "b"), {"stargazers_count": 187, "full_name": "up/stream"}, NOW)
        self.assertTrue(any("probably the canonical project" in w for w in warnings))

    def test_fork_of_a_small_parent_asks_which_is_canonical(self):
        data = {**self.base, "stargazers_count": 182, "fork": True, "parent": {"full_name": "up/stream"}}
        _, warnings = cc.repo_findings(data, ("a", "b"), {"stargazers_count": 1}, NOW)
        self.assertTrue(any("check which one is canonical" in w for w in warnings))

    def test_ecosystems_record_is_reshaped_like_the_github_api(self):
        shaped = cc.from_ecosystems({"full_name": "a/b", "license": "gpl-3.0", "archived": True,
                                     "fork": True, "source_name": "up/stream", "stargazers_count": 5})
        self.assertEqual(shaped["license"], {"spdx_id": "GPL-3.0"})
        self.assertEqual(shaped["parent"], {"full_name": "up/stream"})
        self.assertTrue(shaped["archived"] and shaped["fork"])


class LeadValidationTests(unittest.TestCase):
    def load(self, text: str) -> tuple[list[dict], list[str]]:
        errors: list[str] = []
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "leads.toml"
            path.write_text(text, encoding="utf-8")
            return vl.load_leads(errors, path), errors

    GOOD = ('[[lead]]\nname = "X"\nurl = "https://example.org/x"\nsection = "Datasets"\n'
            'reason = "unverified"\ndate = "2026-10-10"\n')

    def test_missing_file_is_fine(self):
        self.assertEqual(vl.load_leads([], Path("/nonexistent/leads.toml")), [])

    def test_good_record(self):
        records, errors = self.load(self.GOOD)
        self.assertEqual((len(records), errors), (1, []))

    def test_missing_field_and_bad_date_and_http(self):
        _, errors = self.load('[[lead]]\nname = "X"\nurl = "http://e.org/x"\ndate = "10/10/2026"\n')
        text = "\n".join(errors)
        self.assertIn("needs 'section'", text)
        self.assertIn("needs 'reason'", text)
        self.assertIn("YYYY-MM-DD", text)
        self.assertIn("must be https", text)

    def test_duplicate_urls(self):
        _, errors = self.load(self.GOOD + "\n" + self.GOOD)
        self.assertTrue(any("already used by another lead" in e for e in errors))

    def test_unknown_table(self):
        _, errors = self.load('[[leed]]\nname = "X"\n')
        self.assertTrue(any("unknown table" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
