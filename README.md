# Awesome Automotive Security [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A curated Awesome-list for automotive security tools and knowledge. If other better lists exist, we'll try to reference them instead of duplicating work.

Suggestions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for what earns a place on the list.

## Contents

* [CAN Bus Analysis](#can-bus-analysis)
* [Diagnostic Tools](#diagnostic-tools)
* [Firmware and ECU Reverse Engineering](#firmware-and-ecu-reverse-engineering)
* [Automotive Ethernet](#automotive-ethernet)
* [RF and Key Fob Analysis](#rf-and-key-fob-analysis)
* [Infotainment and IVI](#infotainment-and-ivi)
* [V2X Security](#v2x-security)
* [EV Charging Security](#ev-charging-security)
* [Hardware Interfaces](#hardware-interfaces)
* [Security Analysis](#security-analysis)
* [Penetration Testing](#penetration-testing)
* [Datasets](#datasets)
* [Research Papers](#research-papers)
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
* [python-can](https://github.com/hardbyte/python-can) - Python library providing a common interface over many CAN hardware backends with CAN FD support and logging to ASC, BLF, MF4, TRC, CSV, and SQLite.
* [CANalyzat0r](https://github.com/schutzwerk/CANalyzat0r) - Security analysis toolkit for proprietary car protocols with graphical sniffing, fuzzing, packet comparison, background-noise filtering, and UDS fuzzing.
* [canmatrix](https://github.com/ebroecker/canmatrix) - Python package to read and write CAN database formats, converting between DBC, ARXML, KCD, SYM, LDF, ODX, and more.
* [opendbc](https://github.com/commaai/opendbc) - Python API for your car, bundling community-maintained DBC files with CAN parsing and car interface libraries for reading vehicle state and actuating controls.
* [Carpunk](https://github.com/souravbaghz/Carpunk) - CAN injection toolkit and successor to CANghost, automating interface setup, sniffing, replay, and injection attacks.
* [canTot](https://github.com/shipcod3/canTot) - Metasploit-style CAN bus exploitation framework built on sploitkit, packaging published vehicle-specific CAN attacks as selectable modules.

## Diagnostic Tools

* [UDSim](https://github.com/zombieCraig/UDSim) - UDS (Unified Diagnostic Services) ECU simulator and fuzzer for discovering and testing UDS services.
* [VW_Flash](https://github.com/bri3d/VW_Flash) - Flashing tools for VW AG control units over UDS supporting Simos18.1/6/10 and DQ250-MQB.
* [conescan](https://github.com/ConnorRigby/conescan) - Automotive ECU hacking supertool for firmware dumping and manipulation via J2534 OBD interfaces.
* [uds-firmware-extraction](https://github.com/honinb0n/uds-firmware-extraction) - Tool for extracting ECU firmware from UDS flash traffic following ISO-14229 standard.
* [Atlas](https://github.com/kylehulscher/atlas) - Open-source ECU calibration application for reverse engineering and recalibrating Subaru, Toyota, and Honda ECUs, with an integrated Ghidra bundle for analysing tables and emulating ROM machine code.
* [UnlockECU](https://github.com/jglim/UnlockECU) - Free seed-key unlocking tool for Bosch, Continental, Delphi, Daimler, and Marquardt ECUs without proprietary DLLs.
* [Ford-ECU-Bruteforcer](https://github.com/jakka351/Ford-ECU-Bruteforcer) - Security access brute-force tool for pre-2011 Ford ECUs with 3-byte seed and 5-byte key.
* [pq-flasher](https://github.com/I-CAN-hack/pq-flasher) - Python tools for reflashing VW PQ35 EPS using TP 2.0 transport layer and KWP2000 diagnostics.
* [AutoPi](https://github.com/autopi-io/autopi-core) - Open-source core software for the AutoPi dongle, a Raspberry Pi-based OBD-II device for vehicle diagnostics, CAN bus data collection, and automotive IoT applications.
* [gallia](https://github.com/Fraunhofer-AISEC/gallia) - Extendable automotive pentesting framework from Fraunhofer AISEC focused on UDS, with DoIP and ISO-TP transports and structured logging for reproducible scans.
* [udsoncan](https://github.com/pylessard/python-udsoncan) - Python implementation of the ISO 14229 UDS protocol covering session control, security access, data identifiers, and routine control.
* [python-doipclient](https://github.com/jacobschaer/python-doipclient) - Pure Python DoIP (ISO 13400) client that plugs into udsoncan as a transport layer for diagnostics over automotive Ethernet.
* [odxtools](https://github.com/mercedes-benz/odxtools) - Python toolkit for parsing ODX/PDX (ISO 22901) diagnostic databases and encoding, decoding, and snooping ECU diagnostic sessions.

## Firmware and ECU Reverse Engineering

* [Simos18_SBOOT](https://github.com/bri3d/Simos18_SBOOT) - Documented exploit chain against the VW Simos18 supplier bootloader, chaining PWM entry, a weak Mersenne Twister seed/key, and a CRC bounds-check flaw into arbitrary flash read.
* [ghidra-tc1797](https://github.com/christianobora/ghidra-tc1797) - Ghidra processor specification and language definitions for the Infineon TriCore TC1797, used to label memory regions when disassembling MED17 and similar ECU firmware.

## Automotive Ethernet

* [ICS CAP](https://intrepidcs.com/products/software/ics-cap/) - Free Wireshark plugin for monitoring Automotive Ethernet, CAN, CAN FD, LIN, and FlexRay networks.
* [eth-ws-someip](https://github.com/jamores/eth-ws-someip) - Wireshark LUA dissectors for Automotive Ethernet SOME/IP and SOME/IP-SD protocols (Autosar 4.2).
* [Scapy](https://scapy.net/) - Python packet manipulation library with support for DoIP, SOME/IP, AUTOSAR PDUs, SecOC, CAN-FD, and FlexRay protocols.
* [ProtoCrawler](https://cytal.co.uk/) - Intelligent protocol fuzzer for SOME/IP, DoIP, UDS, and Ethernet AVB satisfying ISO/SAE 21434 testing requirements.

## RF and Key Fob Analysis

* [KeyFob Analysis Toolkit (KAT)](https://github.com/KaraZajac/KAT) - Toolkit for analyzing, decoding, and retransmitting key fob signals with support for HackRF, RTL-SDR, and Flipper Zero.
* [Universal Radio Hacker (URH)](https://github.com/jopohl/urh) - Open-source suite for wireless protocol investigation with native SDR support and easy signal demodulation.
* [rtl_433](https://github.com/merbanan/rtl_433) - Generic ISM band receiver for decoding TPMS sensors and key fobs at 315/433/868/915 MHz with RTL-SDR.
* [Flipper Zero](https://flipperzero.one/) - Handheld multi-tool with Sub-GHz capabilities for reading, saving, and transmitting key fob signals with automotive database.
* [Proxmark3](https://proxmark.com/) - Industry-standard RFID/NFC research tool for reading, cloning, and emulating immobilizer transponders at 125kHz and 13.56MHz.
* [Flipper-ARF](https://github.com/D4C1-Labs/Flipper-ARF) - Automotive-focused firmware fork for Flipper Zero supporting Keeloq, rolling codes, and VAG protocol analysis.

## Infotainment and IVI

* [ic1101](https://github.com/librick/ic1101) - Open research project for reverse engineering 10th generation Honda Civic infotainment systems (Android-based, NVIDIA Tegra 3).
* [Chimaera](https://link.springer.com/article/10.1007/s11416-024-00522-4) - Research framework for IVI (In-Vehicle Infotainment) firmware reverse engineering and exploitation targeting Hyundai/Kia Gen5W_L systems.

## V2X Security

* [V2Verifier](https://github.com/twardokus/v2verifier) - Open-source V2X security testbed with first open-source IEEE 1609.2 implementation for DSRC and C-V2X.

## EV Charging Security

* [EVerest](https://github.com/EVerest/everest-core) - Linux Foundation Energy full-stack open-source EV charging firmware implementing OCPP 1.6/2.0.1/2.1, ISO 15118-2/-3/-20, IEC 61851, and DIN SPEC 70121, useful as a reference target and test peer.
* [WWCP_ISO15118](https://github.com/OpenChargingCloud/WWCP_ISO15118) - ISO 15118 implementation covering SLAC, SDP, V2GTP, -2 and -20, explicitly shipping attack vectors and penetration-testing workflows for the individual subprotocols.

## Hardware Interfaces

* [panda](https://github.com/commaai/panda) - Open-source CAN and CAN FD interface firmware from comma.ai running on an STM32H725, with Python bindings for full read/write access to vehicle buses.
* [CANtact](https://github.com/linklayer/cantact-app) - Open-source hardware CAN interface and desktop app supporting live tracing, frame transmission, ISO-TP, JavaScript scripting, and candump-format traces.
* [RAMN](https://github.com/ToyotaInfoTech/RAMN) - Resistant Automotive Miniature Network, a four-ECU CAN/CAN FD testbed on a single board with KiCad sources, CARLA closed-loop simulation, and use as the Car Hacking Village CTF platform.

## Security Analysis

* [QuickTARA](https://github.com/leonkalema/quicktara) - Professional-grade TARA (Threat Analysis and Risk Assessment) tool implementing STRIDE analysis and ISO 21434/UN R155 compliance.
* [Security AutoDesigner](https://plaxidityx.com/products/security-autodesigner/) - Automated TARA platform for creating ISO 21434 and UNR 155 compliant threat analysis reports.
* [AVCDL](https://github.com/nutonomy/AVCDL) - Motional's open-sourced Versatile Cybersecurity Development Lifecycle with process definitions and templates mapped to ISO/SAE 21434, ISO 24089, and UN R155/R156, assessed by TUV SUD.

## Penetration Testing

* [Car Toolkit](https://github.com/j-schmied/car-toolkit) - Python-based toolkit for automotive penetration testing with CAN suite, CARAL, and virtual test bench setup.
* [PiCCANTE](https://github.com/Alia5/PiCCANTE) - Dirt-cheap CAN bus exploration tool built on Raspberry Pi Pico as an open-source hardware/software solution.
* [pwnobd](https://github.com/Nnubes256/pwnobd) - Offensive cybersecurity toolkit for vulnerability analysis of OBD-II devices presented at Black Hat Europe 2024.
* [DongleScope](https://github.com/OSUSecLab/DongleScope) - Automated tool for detecting vulnerabilities in wireless OBD-II dongles based on USENIX Security 2020 research.
* [SecOC Key Extractor](https://github.com/i-can-hack/secoc) - Scripts to extract SecOC (Secure On-Board Communication) keys from Toyota vehicles using comma.ai panda hardware.
* [tesla-opener](https://github.com/rgerganov/tesla-opener) - Open-source tool to open Tesla charging port using HackRF and WebUSB with ASK/OOK RF transmission.
* [automotive-security-research](https://github.com/ps1337/automotive-security-research) - Published reverse engineering results for two production vehicles including CAN matrices, extracted ECU security access keys, and UDS scanning proof-of-concepts.

## Datasets

* [ROAD](https://0xsam.com/road/) - Real ORNL Automotive Dynamometer CAN intrusion dataset with verified fuzzing, targeted ID, masquerade, and accelerator attacks captured on a dynamometer.
* [CAN-MIRGU](https://github.com/sampathrajapaksha/CAN-MIRGU) - CAN bus attack dataset from a modern vehicle driven on real roads over six days, with physically verified masquerade, suspension, and real attacks.
* [Cross-Vehicle Generalisation Benchmark](https://github.com/obaf/Cross-Vehicle-Generalisation-of-In-Vehicle-Intrusion-Detection) - Leave-one-vehicle-out benchmark unifying ROAD, CIDv2, and can-train-and-test into 217 captures across eight vehicles for evaluating whether CAN IDS models transfer.

## Research Papers

Peer-reviewed research and landmark industry reports, ordered by year of
publication. Open-access copies are linked where one exists.
* [Security in Automotive Bus Systems](https://www.weimerskirch.org/files/WolfEtAl_SecureBus.pdf) - Wolf, Weimerskirch, and Paar, Workshop on Embedded Security in Cars 2004. The first systematic treatment of CAN, LIN, MOST, and FlexRay as security problems, proposing the gateway and cryptographic measures later echoed in SecOC.
* [Securing Vehicular Ad Hoc Networks](https://infoscience.epfl.ch/entities/publication/2976e5d8-215b-4465-834e-875efe55844f) - Raya and Hubaux, Journal of Computer Security 2007. Threat analysis and security architecture for VANETs that set the direction for most later V2X security work.
* [Secure Vehicular Communication Systems: Design and Architecture](https://arxiv.org/abs/0912.5391) - Papadimitratos et al., IEEE Communications Magazine 2008. The SeVeCom architecture, which defined the certificate and pseudonym model underlying today's V2X security stacks.
* [Experimental Security Analysis of a Modern Automobile](https://www.autosec.org/pubs/cars-oakland2010.pdf) - Koscher et al., IEEE S&P 2010. The paper that opened the field, demonstrating that an attacker with access to any single ECU can disable the brakes and stop the engine of a moving vehicle.
* [Security and Privacy Vulnerabilities of In-Car Wireless Networks: A Tire Pressure Monitoring System Case Study](https://www.usenix.org/conference/usenixsecurity10/security-and-privacy-vulnerabilities-car-wireless-networks-tire-pressure) - Rouf et al., USENIX Security 2010. Shows TPMS sensors are unauthenticated and trackable at roughly 40m, the first published wireless in-car network attack.
* [Comprehensive Experimental Analyses of Automotive Attack Surfaces](https://www.usenix.org/conference/usenix-security-11/comprehensive-experimental-analyses-automotive-attack-surfaces) - Checkoway et al., USENIX Security 2011. Follow-up establishing the remote attack surface, compromising a vehicle over Bluetooth, cellular, and the CD player.
* [Relay Attacks on Passive Keyless Entry and Start Systems in Modern Cars](https://www.ndss-symposium.org/ndss2011/relay-attacks-on-passive-keyless-entry-and-start-systems-in-modern-cars/) - Francillon, Danev, and Capkun, NDSS 2011. Demonstrates the relay attack that still underpins most keyless vehicle theft today, against ten PKES systems from eight manufacturers.
* [Gone in 360 Seconds: Hijacking with Hitag2](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/verdult) - Verdult, Garcia, and Balasch, USENIX Security 2012. Breaks the Hitag2 immobilizer transponder, then fitted to over 200 car models, recovering the key by radio in minutes.
* [Adventures in Automotive Networks and Control Units](https://illmatics.com/car_hacking.pdf) - Miller and Valasek, 2013. The wired precursor to the Jeep work, documenting CAN injection against the Toyota Prius and Ford Escape and the methodology that followed.
* [Survey on Security Threats and Protection Mechanisms in Embedded Automotive Networks](https://ieeexplore.ieee.org/document/6615528/) - Studnia et al., DSN Workshops 2013. Widely cited survey mapping in-vehicle protocols, the threats against them, and candidate countermeasures.
* [Dismantling Megamos Crypto: Wirelessly Lockpicking a Vehicle Immobilizer](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/verdult) - Verdult, Garcia, and Ege, USENIX Security 2015. Reverse engineers the Megamos immobilizer used by Audi, Fiat, Honda, Volkswagen, and Volvo; famously injuncted for two years before publication.
* [Remote Exploitation of an Unaltered Passenger Vehicle](https://www.ioactive.com/wp-content/uploads/pdfs/IOActive_Remote_Car_Hacking.pdf) - Miller and Valasek, 2015. The Jeep Cherokee cellular-to-CAN attack chain that triggered a 1.4 million vehicle recall.
* [Fast and Vulnerable: A Story of Telematic Failures](https://www.usenix.org/conference/woot15/workshop-program/presentation/foster) - Foster, Prudhomme, Koscher, and Savage, USENIX WOOT 2015. Shows an aftermarket OBD-II telematics dongle exposing SMS-reachable remote control of vehicle CAN traffic.
* [Potential Cyberattacks on Automated Vehicles](https://its.berkeley.edu/publications/potential-cyberattacks-automated-vehicles) - Petit and Shladover, IEEE T-ITS 2015. The standard reference taxonomy of attack vectors against autonomous and cooperative automated vehicles.
* [Remote Attacks on Automated Vehicles Sensors: Experiments on Camera and LiDAR](https://blackhat.com/docs/eu-15/materials/eu-15-Petit-Self-Driving-And-Connected-Cars-Fooling-Sensors-And-Tracking-Drivers-wp1.pdf) - Petit, Stottelaar, Feiri, and Kargl, Black Hat Europe 2015. First practical spoofing and blinding of automotive camera and LiDAR using commodity hardware.
* [Pseudonym Schemes in Vehicular Networks: A Survey](https://oparu.uni-ulm.de/items/b215d57b-06e1-4f27-a67e-a6ecaf3b45d2) - Petit, Schaub, Feiri, and Kargl, IEEE Communications Surveys and Tutorials 2015. Defines the pseudonym lifecycle and categorises the schemes that reconcile V2X message authentication with driver privacy.
* [Fingerprinting Electronic Control Units for Vehicle Intrusion Detection](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/cho) - Cho and Shin, USENIX Security 2016. Clock-based IDS that fingerprints ECUs from clock skew in periodic messages, the most-replicated CAN IDS baseline.
* [Error Handling of In-vehicle Networks Makes Them Vulnerable](https://dl.acm.org/doi/10.1145/2976749.2978302) - Cho and Shin, ACM CCS 2016. The bus-off attack, which abuses CAN error handling to force an uncompromised ECU off the bus without any vehicle-specific reverse engineering.
* [Lock It and Still Lose It: On the (In)Security of Automotive Remote Keyless Entry Systems](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/garcia) - Garcia, Oswald, Kasper, and Pavlides, USENIX Security 2016. Recovers shared global keys covering most Volkswagen Group vehicles sold over two decades, and breaks the Hitag2 rolling-code scheme.
* [vatiCAN: Vetted, Authenticated CAN Bus](https://christian-rossow.de/publications/vatican-ches2016.pdf) - Nurnberger and Rossow, CHES 2016. Retrofit authentication for CAN using MACs and a global nonce, a reference point for later SecOC-style designs.
* [LeiA: A Lightweight Authentication Protocol for CAN](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/29342174/leia.pdf) - Radu and Garcia, ESORICS 2016. Backwards-compatible per-ID authentication that fits CAN's timing and bandwidth limits, compartmentalising ECUs so a compromised head unit cannot actuate the powertrain.
* [Illusion and Dazzle: Adversarial Optical Channel Exploits Against Lidars for Automotive Applications](https://eprint.iacr.org/2017/613) - Shin, Kim, Kwon, and Kim, CHES 2017. Saturates and spoofs an automotive LiDAR over its optical channel, creating fake points and blinding it entirely.
* [Viden: Attacker Identification on In-Vehicle Networks](https://arxiv.org/abs/1708.08414) - Cho and Shin, ACM CCS 2017. Fingerprints transmitting ECUs by their analogue voltage signature, moving CAN defence from detecting an attack to naming the ECU responsible.
* [WALNUT: Waging Doubt on the Integrity of MEMS Accelerometers with Acoustic Injection Attacks](https://spqrlab1.github.io/papers/trippel-IEEE-oaklawn-walnut-2017.pdf) - Trippel, Weisse, Xu, Honeyman, and Fu, IEEE EuroS&P 2017. Acoustic resonance attacks that forge accelerometer output, establishing analogue sensor integrity as its own threat model.
* [VulCAN: Efficient Component Authentication and Software Isolation for Automotive Control Networks](https://vanbulck.net/files/acsac17-vulcan.pdf) - Van Bulck, Muhlberg, and Piessens, ACSAC 2017. Combines message authentication with trusted-computing isolation, defending against an adversary running arbitrary code on a participating ECU.
* [GIDS: GAN based Intrusion Detection System for In-Vehicle Network](https://arxiv.org/abs/1907.07377) - Seo, Song, and Kim, PST 2018. Trains a GAN on normal CAN traffic only, and is a common deep-learning IDS baseline alongside the authors' Car-Hacking dataset.
* [Beneath the Bonnet: A Breakdown of Diagnostic Security](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/50643148/Beneath_the_Bonnet.pdf) - Van den Herrewegen and Garcia, ESORICS 2018. Reverse engineers the seed-key ciphers of four manufacturers from ECU firmware and achieves remote code execution over CAN through diagnostics alone.
* [Robust Physical-World Attacks on Deep Learning Visual Classification](https://arxiv.org/abs/1707.08945) - Eykholt et al., CVPR 2018. The stop-sign sticker attack, the canonical physical adversarial example against road sign recognition.
* [All Your GPS Are Belong To Us: Towards Stealthy Manipulation of Road Navigation Systems](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng) - Zeng et al., USENIX Security 2018. Spoofs GPS to reroute a driver to an attacker-chosen destination while keeping the displayed route plausible.
* [CANvas: Fast and Inexpensive Automotive Network Mapping](https://www.usenix.org/conference/usenixsecurity19/presentation/kulandaivel) - Kulandaivel, Goyal, Agrawal, and Sekar, USENIX Security 2019. Builds an nmap for the vehicle, recovering the sender and receiver map of a CAN network in under an hour using clock offsets and forced ECU isolation.
* [Losing the Car Keys: Wireless PHY-Layer Insecurity in EV Charging](https://www.usenix.org/conference/usenixsecurity19/presentation/baker) - Baker and Martinovic, USENIX Security 2019. Recovers ISO 15118 charging messages from the unintentional wireless emissions of CCS power-line communication across 54 real charging sessions.
* [Fast, Furious and Insecure: Passive Keyless Entry and Start Systems in Modern Supercars](https://tches.iacr.org/index.php/TCHES/article/view/8289) - Wouters et al., CHES 2019. Breaks the DST40-based PKES used by Tesla and others, cloning a key fob from a few seconds of proximity.
* [Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826) - Cao et al., ACM CCS 2019. Spoofs LiDAR returns to inject a fake obstacle into the perception pipeline of a production autonomous driving stack.
* [Plug-N-Pwned: Comprehensive Vulnerability Analysis of OBD-II Dongles](https://www.usenix.org/conference/usenixsecurity20/presentation/wen) - Wen, Chen, and Lin, USENIX Security 2020. Automated analysis of 77 wireless OBD-II dongles, every one of which exposed at least two vulnerability classes.
* [A Comprehensive Guide to CAN IDS Data and Introduction of the ROAD Dataset](https://arxiv.org/abs/2012.14600) - Verma et al., 2020. Systematises the CAN IDS dataset landscape, documents the flaws in earlier datasets, and introduces ROAD.
* [Automated Cross-Platform Reverse Engineering of CAN Bus Commands From Mobile Apps](https://www.ndss-symposium.org/ndss-paper/automated-cross-platform-reverse-engineering-of-can-bus-commands-from-mobile-apps/) - Wen, Zhao, Chen, and Lin, NDSS 2020. Recovers CAN command syntax and semantics for 360 car models from companion mobile apps alone, without touching a vehicle.
* [Drift with Devil: Security of Multi-Sensor Fusion based Localization in High-Level Autonomous Driving under GPS Spoofing](https://www.usenix.org/conference/usenixsecurity20/presentation/shen) - Shen et al., USENIX Security 2020. Shows sensor fusion does not neutralise GPS spoofing, taking an autonomous vehicle off its lane with gradual position drift.
* [My Other Car is Your Car: Compromising the Tesla Model X Keyless Entry System](https://tches.iacr.org/index.php/TCHES/article/view/9063) - Wouters, Gierlichs, and Preneel, CHES 2021. Chains a BLE firmware downgrade and a key fob update flaw into unlocking and driving away a Tesla Model X.
* [Dirty Road Can Attack: Security of Deep Learning based Automated Lane Centering under Physical-World Attack](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) - Sato et al., USENIX Security 2021. Physical dirty-road patches that steer a production lane-centering system out of its lane.
* [Too Good to Be Safe: Tricking Lane Detection in Autonomous Driving with Crafted Perturbations](https://www.usenix.org/conference/usenixsecurity21/presentation/jing) - Jing et al., USENIX Security 2021. First lane-detection attack validated on a real production vehicle, exploiting the module's over-sensitivity with small road markings.
* [Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion based Perception in Autonomous Driving](https://arxiv.org/abs/2106.09249) - Cao et al., IEEE S&P 2021. Defeats the multi-sensor fusion designs that production stacks actually use, with a single adversarial object invisible to camera and LiDAR at once.
* [Exposing New Vulnerabilities of Error Handling Mechanism in CAN](https://www.usenix.org/conference/usenixsecurity21/presentation/serag) - Serag et al., USENIX Security 2021. Systematically tests CAN node behaviour under error conditions with CANOX and finds three further vulnerabilities in the standard beyond the bus-off attack.
* [Evading Voltage-Based Intrusion Detection on Automotive CAN](https://www.ndss-symposium.org/ndss-paper/evading-voltage-based-intrusion-detection-on-automotive-can/) - Bhatia et al., NDSS 2021. The DUET masquerade attack, in which two compromised ECUs corrupt the bus voltage and defeat every published voltage-based IDS, including Viden.
* [Brokenwire: Wireless Disruption of CCS Electric Vehicle Charging](https://www.ndss-symposium.org/ndss-paper/brokenwire-wireless-disruption-of-ccs-electric-vehicle-charging/) - Kohler, Baker, Strohmeier, and Martinovic, NDSS 2023. Aborts CCS rapid-charging sessions wirelessly from tens of metres with off-the-shelf radio hardware, against individual vehicles or whole fleets.

## Learning Resources

* [Automotive Security Timeline](https://github.com/automotive-security/Automotive-Security-Timeline) - Continuously updated knowledge base of automotive cybersecurity events including vulnerability disclosures, attack demonstrations, Pwn2Own Automotive results, and supply-chain incidents.
* [Automotive-Networking-Security](https://automotive-network-security.com/standard_solutions.shtml) - Automotive networking security standards and solutions overview.
* [What is Automotive MACsec?](https://youtu.be/5QiHmMoJCOE) - Video training on Automotive MACsec concepts by Technica Engineering.
* [The Car Hacker's Handbook](https://www.opengarages.org/handbook/) - Craig Smith's foundational book on vehicle security, free to read online via Open Garages.
* [Car Hacking Village](https://www.carhackingvillage.com/events) - Non-profit running hands-on car hacking workshops and CTFs at DEF CON, Black Hat, HITCON, CODE BLUE, and other conferences.
* [Automotive Cybersecurity Roadmap](https://github.com/AutoSecurityy/Automotive-Cybersecurity-Roadmap) - Structured learning path from CAN and UDS fundamentals through TARA, firmware reverse engineering, and hardware hacking into specialized career tracks.

## Related Awesome Lists

* [Awesome Embedded Security](https://github.com/hexsecs/awesome-embedded-security) - Tools and knowledge for embedded security research.
* [Awesome CANbus](https://github.com/iDoka/awesome-canbus) - Comprehensive CAN bus security resources.
* [Awesome CANb IDs](https://github.com/iDoka/awesome-automotive-can-id) - CAN bus ID reference and documentation.
* [Awesome Vehicle Security](https://github.com/jaredthecoder/awesome-vehicle-security) - Long-running curated list of vehicle security resources, hardware, software, researchers, and manufacturer disclosure programs.
* [Awesome EV Charging](https://github.com/juherr/awesome-ev-charging) - Curated specifications, tools, and resources for EV charging protocols including OCPP, ISO 15118, OCPI, and Eichrecht.
* [Awesome Connected Things Sec](https://github.com/V33RU/awesome-connected-things-sec) - Security resources across IoT, embedded, industrial, and automotive systems with a dedicated automotive section.
