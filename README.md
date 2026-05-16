# Awesome Automotive Security [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A curated Awesome-list for automotive security tools and knowledge. If other better lists exist, we'll try to reference them instead of duplicating work.

## Table of Contents

* [CAN Bus Analysis](#can-bus-analysis)
* [Diagnostic Tools](#diagnostic-tools)
* [Automotive Ethernet](#automotive-ethernet)
* [RF and Key Fob Analysis](#rf-and-key-fob-analysis)
* [Infotainment and IVI](#infotainment-and-ivi)
* [V2X Security](#v2x-security)
* [Security Analysis](#security-analysis)
* [Penetration Testing](#penetration-testing)
* [Learning Resources](#learning-resources)
* [Related Awesome Lists](#related-awesome-lists)

## CAN Bus Analysis

* [can-utils](https://github.com/linux-can/can-utils) - Linux-CAN SocketCAN userspace utilities including cansniffer, candump, cansend, canplayer, and cangen for CAN bus analysis.
* [SavvyCAN](https://github.com/collin80/SavvyCAN) - Cross-platform Qt-based CAN bus reverse engineering and capture tool with DBC file loading, UDS scanning, and fuzzing support.
* [Kayak](https://github.com/dschanoeh/Kayak) - Java-based CAN bus analysis tool with bus monitoring and DBC/KCD file loading support.
* [ICSim](https://github.com/zombieCraig/ICSim) - Instrument Cluster Simulator for safe CAN bus security testing with virtual dashboard controls.
* [CANToolz](https://github.com/CANToolz/CANToolz) - Black-box CAN network analysis framework also known as YACHT with modular architecture for fuzzing and ECU discovery.
* [cantools](https://github.com/cantools/cantools) - Python library for CAN bus diagnostics, DBC parsing, and message decoding/encoding.
* [Lindwurm](https://github.com/lindwurm-can/lindwurm) - Open-source CAN bus tracing and fuzzing tool designed for penetration testing with Burp Suite-inspired workflow.
* [CANgaroo](https://github.com/wikilift/CANgaroo) - Open-source CAN bus analyzer with transmit/receive support for standard and FD frames plus DBC decoding.
* [CaringCaribou](https://github.com/CaringCaribou/caringcaribou) - Python automotive security exploration tool designed as the nmap of CAN bus with fuzzing, ECU discovery, and attack modules.
* [CANalyse](https://github.com/canalyse/CANalyse-2.0) - Vehicle network analysis tool with SQL-like queries on CAN data, smart signal scanning, and Telegram bot integration.
* [CANter](https://ceur-ws.org/Vol-3962/paper69.pdf) - Intrusion detection system for CAN and CAN-FD that detects drop-and-spoof attacks using frequency analysis of frame intervals.
* [OBDium](https://github.com/provrb/obdium) - Rust-based OBD-II diagnostic tool with modern Tauri GUI supporting live data, DTC analysis, and offline VIN decoding.

## Diagnostic Tools

* [UDSim](https://github.com/zombieCraig/UDSim) - UDS (Unified Diagnostic Services) ECU simulator and fuzzer for discovering and testing UDS services.
* [VW_Flash](https://github.com/bri3d/VW_Flash) - Flashing tools for VW AG control units over UDS supporting Simos18.1/6/10 and DQ250-MQB.
* [conescan](https://github.com/ConnorRigby/conescan) - Automotive ECU hacking supertool for firmware dumping and manipulation via J2534 OBD interfaces.
* [uds-firmware-extraction](https://github.com/honinb0n/uds-firmware-extraction) - Tool for extracting ECU firmware from UDS flash traffic following ISO-14229 standard.
* [Atlas](https://github.com/atlas-tuning/atlas) - Open-source ECU calibration application for Subaru and Toyota with Ghidra integration for firmware analysis.
* [UnlockECU](https://github.com/jglim/UnlockECU) - Free seed-key unlocking tool for Bosch, Continental, Delphi, Daimler, and Marquardt ECUs without proprietary DLLs.
* [Ford-ECU-Bruteforcer](https://github.com/jakka351/Ford-ECU-Bruteforcer) - Security access brute-force tool for pre-2011 Ford ECUs with 3-byte seed and 5-byte key.
* [pq-flasher](https://github.com/I-CAN-hack/pq-flasher) - Python tools for reflashing VW PQ35 EPS using TP 2.0 transport layer and KWP2000 diagnostics.
* [AutoPi](https://github.com/autopi-io/autopi-core) - Open-source core software for the AutoPi dongle, a Raspberry Pi-based OBD-II device for vehicle diagnostics, CAN bus data collection, and automotive IoT applications.

## Automotive Ethernet

* [ICS CAP](https://intrepidcs.com/products/software/ics-cap/) - Free Wireshark plugin for monitoring Automotive Ethernet, CAN, CAN FD, LIN, and FlexRay networks.
* [eth-ws-someip](https://github.com/jamores/eth-ws-someip) - Wireshark LUA dissectors for Automotive Ethernet SOME/IP and SOME/IP-SD protocols (Autosar 4.2).
* [Scapy](https://scapy.net/) - Python packet manipulation library with support for DoIP, SOME/IP, AUTOSAR PDUs, SecOC, CAN-FD, and FlexRay protocols.
* [ProtoCrawler](https://cytal.co.uk/) - Intelligent protocol fuzzer for SOME/IP, DoIP, UDS, and Ethernet AVB satisfying ISO/SAE 21434 testing requirements.

## RF and Key Fob Analysis

* [KeyFob Analysis Toolkit (KAT)](https://github.com/KaraZajac/KAT) - Toolkit for analyzing, decoding, and retransmitting key fob signals with support for HackRF, RTL-SDR, and Flipper Zero.
* [Universal Radio Hacker (URH)](https://github.com/miek/urh) - Open-source suite for wireless protocol investigation with native SDR support and easy signal demodulation.
* [rtl_433](https://github.com/merbanan/rtl_433) - Generic ISM band receiver for decoding TPMS sensors and key fobs at 315/433/868/915 MHz with RTL-SDR.
* [Flipper Zero](https://flipperzero.one/) - Handheld multi-tool with Sub-GHz capabilities for reading, saving, and transmitting key fob signals with automotive database.
* [Proxmark3](https://proxmark.com/) - Industry-standard RFID/NFC research tool for reading, cloning, and emulating immobilizer transponders at 125kHz and 13.56MHz.
* [Flipper-ARF](https://github.com/D4C1-Labs/Flipper-ARF) - Automotive-focused firmware fork for Flipper Zero supporting Keeloq, rolling codes, and VAG protocol analysis.

## Infotainment and IVI

* [ic1101](https://github.com/librick/ic1101) - Open research project for reverse engineering 10th generation Honda Civic infotainment systems (Android-based, NVIDIA Tegra 3).
* [Chimaera](https://link.springer.com/article/10.1007/s11416-024-00522-4) - Research framework for IVI (In-Vehicle Infotainment) firmware reverse engineering and exploitation targeting Hyundai/Kia Gen5W_L systems.

## V2X Security

* [V2Verifier](https://github.com/twardokus/v2verifier) - Open-source V2X security testbed with first open-source IEEE 1609.2 implementation for DSRC and C-V2X.

## Security Analysis

* [QuickTARA](https://github.com/leonkalema/quicktara) - Professional-grade TARA (Threat Analysis and Risk Assessment) tool implementing STRIDE analysis and ISO 21434/UN R155 compliance.
* [Security AutoDesigner](https://plaxidityx.com/products/security-autodesigner/) - Automated TARA platform for creating ISO 21434 and UNR 155 compliant threat analysis reports.

## Penetration Testing

* [Car Toolkit](https://github.com/j-schmied/car-toolkit) - Python-based toolkit for automotive penetration testing with CAN suite, CARAL, and virtual test bench setup.
* [PiCCANTE](https://github.com/Alia5/PiCCANTE) - Dirt-cheap CAN bus exploration tool built on Raspberry Pi Pico as an open-source hardware/software solution.
* [pwnobd](https://github.com/Nnubes256/pwnobd) - Offensive cybersecurity toolkit for vulnerability analysis of OBD-II devices presented at Black Hat Europe 2024.
* [DongleScope](https://github.com/OSUSecLab/DongleScope) - Automated tool for detecting vulnerabilities in wireless OBD-II dongles based on USENIX Security 2020 research.
* [SecOC Key Extractor](https://github.com/i-can-hack/secoc) - Scripts to extract SecOC (Secure On-Board Communication) keys from Toyota vehicles using comma.ai panda hardware.
* [tesla-opener](https://github.com/rgerganov/tesla-opener) - Open-source tool to open Tesla charging port using HackRF and WebUSB with ASK/OOK RF transmission.

## Learning Resources

* [Automotive Security Timeline](https://github.com/delikely/Automotive-Security-Timeline) - Timeline of automotive security research and vulnerabilities.
* [Automotive-Networking-Security](https://automotive-network-security.com/standard_solutions.shtml) - Automotive networking security standards and solutions overview.
* [What is Automotive MACsec?](https://youtu.be/5QiHmMoJCOE) - Video training on Automotive MACsec concepts by Technica Engineering.

## Related Awesome Lists

* [Awesome Embedded Security](https://github.com/hexsecs/awesome-embedded-security) - Tools and knowledge for embedded security research.
* [Awesome CANbus](https://github.com/iDoka/awesome-canbus) - Comprehensive CAN bus security resources.
* [Awesome CANb IDs](https://github.com/iDoka/awesome-automotive-can-id) - CAN bus ID reference and documentation.
