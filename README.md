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
* [Books](#books)
* [Learning Resources](#learning-resources)
* [Related Awesome Lists](#related-awesome-lists)

## CAN Bus Analysis

* [BUSMASTER](https://github.com/rbei-etas/busmaster) - Open-source CAN simulation, analysis, and test tool from Bosch Engineering and ETAS, with a node simulator, DBC-driven signal interpretation, and scriptable test automation.
* [CAN Commander](https://github.com/MatthewKuKanich/CAN_Commander) - Flipper Zero application and companion ESP32 CAN board for reverse engineering vehicle networks, with sniffing, DBC decoding, replay, and injection profiles usable without a laptop.
* [can-utils](https://github.com/linux-can/can-utils) - Linux-CAN SocketCAN userspace utilities including cansniffer, candump, cansend, canplayer, and cangen for CAN bus analysis.
* [CANalyse](https://github.com/canalyse/CANalyse-2.0) - Vehicle network analysis tool with SQL-like queries on CAN data, smart signal scanning, and Telegram bot integration.
* [CANalyzat0r](https://github.com/schutzwerk/CANalyzat0r) - Security analysis toolkit for proprietary car protocols with graphical sniffing, fuzzing, packet comparison, background-noise filtering, and UDS fuzzing.
* [CANarchy](https://github.com/hexsecs/canarchy) - Stream-first CAN and J1939 toolkit that emits structured JSONL for automation, with live capture, DBC/ARXML/KCD decoding, J1939 PGN/SPN and DM1 fault parsing, UDS and DoIP support, constrained fuzzing, and an MCP server for agent-driven workflows.
* [CANdevStudio](https://github.com/GENIVI/CANdevStudio) - Flow-based graphical CAN simulation environment that wires senders, receivers, DBC decoders, and signal viewers together to stand in for missing ECUs on a bench.
* [CANflict](https://github.com/necst/CANflict) - C library that manipulates the CAN bus at the data link layer from an unmodified microcontroller, abusing pin conflicts between peripherals to craft polyglot frames; the implementation behind the CCS 2022 paper.
* [CANgaroo](https://github.com/wikilift/CANgaroo) - Open-source CAN bus analyzer with transmit/receive support for standard and FD frames plus DBC decoding.
* [canmatrix](https://github.com/ebroecker/canmatrix) - Python package to read and write CAN database formats, converting between DBC, ARXML, KCD, SYM, LDF, ODX, and more.
* [cannelloni](https://github.com/mguentner/cannelloni) - Tunnels SocketCAN interfaces over UDP, TCP, or SCTP, bridging a vehicle bus to a remote analysis machine and letting bench setups share one physical CAN adapter.
* [CANter](https://ceur-ws.org/Vol-3962/paper69.pdf) - Intrusion detection system for CAN and CAN-FD that detects drop-and-spoof attacks using frequency analysis of frame intervals.
* [cantools](https://github.com/cantools/cantools) - Python library for CAN bus diagnostics, DBC parsing, and message decoding/encoding.
* [CANToolz](https://github.com/CANToolz/CANToolz) - Black-box CAN network analysis framework also known as YACHT with modular architecture for fuzzing and ECU discovery.
* [canTot](https://github.com/shipcod3/canTot) - Metasploit-style CAN bus exploitation framework built on sploitkit, packaging published vehicle-specific CAN attacks as selectable modules.
* [CaringCaribou](https://github.com/CaringCaribou/caringcaribou) - Python automotive security exploration tool designed as the nmap of CAN bus with fuzzing, ECU discovery, and attack modules.
* [Carpunk](https://github.com/souravbaghz/Carpunk) - CAN injection toolkit and successor to CANghost, automating interface setup, sniffing, replay, and injection attacks.
* [ICSim](https://github.com/zombieCraig/ICSim) - Instrument Cluster Simulator for safe CAN bus security testing with virtual dashboard controls.
* [Kayak](https://github.com/dschanoeh/Kayak) - Java-based CAN bus analysis tool with bus monitoring and DBC/KCD file loading support.
* [Lindwurm](https://github.com/lindwurm-can/lindwurm) - Open-source CAN bus tracing and fuzzing tool designed for penetration testing with Burp Suite-inspired workflow.
* [OBDium](https://github.com/provrb/obdium) - Rust-based OBD-II diagnostic tool with modern Tauri GUI supporting live data, DTC analysis, and offline VIN decoding.
* [opendbc](https://github.com/commaai/opendbc) - Python API for your car, bundling community-maintained DBC files with CAN parsing and car interface libraries for reading vehicle state and actuating controls.
* [python-can](https://github.com/hardbyte/python-can) - Python library providing a common interface over many CAN hardware backends with CAN FD support and logging to ASC, BLF, MF4, TRC, CSV, and SQLite.
* [SavvyCAN](https://github.com/collin80/SavvyCAN) - Cross-platform Qt-based CAN bus reverse engineering and capture tool with DBC file loading, UDS scanning, and fuzzing support.

## Diagnostic Tools

* [Atlas](https://github.com/kylehulscher/atlas) - Open-source ECU calibration application for reverse engineering and recalibrating Subaru, Toyota, and Honda ECUs, with an integrated Ghidra bundle for analysing tables and emulating ROM machine code.
* [AutoPi](https://github.com/autopi-io/autopi-core) - Open-source core software for the AutoPi dongle, a Raspberry Pi-based OBD-II device for vehicle diagnostics, CAN bus data collection, and automotive IoT applications.
* [conescan](https://github.com/ConnorRigby/conescan) - Automotive ECU hacking supertool for firmware dumping and manipulation via J2534 OBD interfaces.
* [Ford-ECU-Bruteforcer](https://github.com/jakka351/Ford-ECU-Bruteforcer) - Security access brute-force tool for pre-2011 Ford ECUs with 3-byte seed and 5-byte key.
* [gallia](https://github.com/Fraunhofer-AISEC/gallia) - Extendable automotive pentesting framework from Fraunhofer AISEC focused on UDS, with DoIP and ISO-TP transports and structured logging for reproducible scans.
* [odxtools](https://github.com/mercedes-benz/odxtools) - Python toolkit for parsing ODX/PDX (ISO 22901) diagnostic databases and encoding, decoding, and snooping ECU diagnostic sessions.
* [pq-flasher](https://github.com/I-CAN-hack/pq-flasher) - Python tools for reflashing VW PQ35 EPS using TP 2.0 transport layer and KWP2000 diagnostics.
* [python-doipclient](https://github.com/jacobschaer/python-doipclient) - Pure Python DoIP (ISO 13400) client that plugs into udsoncan as a transport layer for diagnostics over automotive Ethernet.
* [uds-firmware-extraction](https://github.com/honinb0n/uds-firmware-extraction) - Tool for extracting ECU firmware from UDS flash traffic following ISO-14229 standard.
* [UDSim](https://github.com/zombieCraig/UDSim) - UDS (Unified Diagnostic Services) ECU simulator and fuzzer for discovering and testing UDS services.
* [udsoncan](https://github.com/pylessard/python-udsoncan) - Python implementation of the ISO 14229 UDS protocol covering session control, security access, data identifiers, and routine control.
* [UnlockECU](https://github.com/jglim/UnlockECU) - Free seed-key unlocking tool for Bosch, Continental, Delphi, Daimler, and Marquardt ECUs without proprietary DLLs.
* [VW_Flash](https://github.com/bri3d/VW_Flash) - Flashing tools for VW AG control units over UDS supporting Simos18.1/6/10 and DQ250-MQB.

## Firmware and ECU Reverse Engineering

* [ghidra-tc1797](https://github.com/christianobora/ghidra-tc1797) - Ghidra processor specification and language definitions for the Infineon TriCore TC1797, used to label memory regions when disassembling MED17 and similar ECU firmware.
* [medc17-checksum-tool](https://github.com/ConnorHowell/medc17-checksum-tool) - Analyses and corrects CRC32, ADD32, and ADD16 checksums in Bosch MED17 and EDC17 firmware, resolving CRC values algebraically rather than by brute force and regenerating RSA signatures after modification.
* [pyA2L](https://github.com/christoph2/pya2l) - Python parser for ASAM MCD-2 MC (A2L) description files, exposing the characteristic, measurement, and memory-layout metadata needed to make sense of ECU calibration data during firmware analysis.
* [Simos18_SBOOT](https://github.com/bri3d/Simos18_SBOOT) - Documented exploit chain against the VW Simos18 supplier bootloader, chaining PWM entry, a weak Mersenne Twister seed/key, and a CRC bounds-check flaw into arbitrary flash read.
* [TC1791_CAN_BSL](https://github.com/bri3d/TC1791_CAN_BSL) - CAN bootstrap loader for Infineon TriCore AudoMAX parts such as the TC1791, giving arbitrary flash and RAM read/write on Simos18 and related ECUs without desoldering.

## Automotive Ethernet

* [eth-ws-someip](https://github.com/jamores/eth-ws-someip) - Wireshark LUA dissectors for Automotive Ethernet SOME/IP and SOME/IP-SD protocols (Autosar 4.2).
* [ICS CAP](https://intrepidcs.com/products/software/ics-cap/) - Free Wireshark plugin for monitoring Automotive Ethernet, CAN, CAN FD, LIN, and FlexRay networks.
* [ProtoCrawler](https://cytal.co.uk/) - Intelligent protocol fuzzer for SOME/IP, DoIP, UDS, and Ethernet AVB satisfying ISO/SAE 21434 testing requirements.
* [Scapy](https://scapy.net/) - Python packet manipulation library with support for DoIP, SOME/IP, AUTOSAR PDUs, SecOC, CAN-FD, and FlexRay protocols.
* [someip-protocol-fuzzer](https://github.com/cfanatic/someip-protocol-fuzzer) - Black-box SOME/IP fuzzer that mutates user-defined protocol fields with radamsa and uses a ping heartbeat to detect when the target service stops responding.
* [vsomeip](https://github.com/COVESA/vsomeip) - COVESA reference implementation of SOME/IP and SOME/IP-SD, used both as the target in automotive Ethernet fuzzing research and as a client for crafting service calls against production ECUs.

## RF and Key Fob Analysis

* [Flipper Zero](https://flipperzero.one/) - Handheld multi-tool with Sub-GHz capabilities for reading, saving, and transmitting key fob signals with automotive database.
* [Flipper-ARF](https://github.com/D4C1-Labs/Flipper-ARF) - Automotive-focused firmware fork for Flipper Zero supporting Keeloq, rolling codes, and VAG protocol analysis.
* [KeyFob Analysis Toolkit (KAT)](https://github.com/KaraZajac/KAT) - Toolkit for analyzing, decoding, and retransmitting key fob signals with support for HackRF, RTL-SDR, and Flipper Zero.
* [Proxmark3](https://proxmark.com/) - Industry-standard RFID/NFC research tool for reading, cloning, and emulating immobilizer transponders at 125kHz and 13.56MHz.
* [rtl_433](https://github.com/merbanan/rtl_433) - Generic ISM band receiver for decoding TPMS sensors and key fobs at 315/433/868/915 MHz with RTL-SDR.
* [Universal Radio Hacker (URH)](https://github.com/jopohl/urh) - Open-source suite for wireless protocol investigation with native SDR support and easy signal demodulation.

## Infotainment and IVI

* [Chimaera](https://link.springer.com/article/10.1007/s11416-024-00522-4) - Research framework for IVI (In-Vehicle Infotainment) firmware reverse engineering and exploitation targeting Hyundai/Kia Gen5W_L systems.
* [ic1101](https://github.com/librick/ic1101) - Open research project for reverse engineering 10th generation Honda Civic infotainment systems (Android-based, NVIDIA Tegra 3).

## V2X Security

* [Artery](https://github.com/riebl/artery) - OMNeT++ simulation framework pairing the Vanetza ITS-G5 stack with SUMO traffic, providing the environment that most misbehavior-detection and V2X attack studies are built on.
* [F2MD](https://github.com/josephkamel/F2MD) - Simulation framework recreating the whole misbehavior detection chain for ITS-G5 and C-V2X, with plausibility checks, machine learning detectors, and both local and global attack implementations.
* [V2Verifier](https://github.com/twardokus/v2verifier) - Open-source V2X security testbed with first open-source IEEE 1609.2 implementation for DSRC and C-V2X.
* [VaN3Twin](https://github.com/DriveX-devs/VaN3Twin) - ETSI-compliant multi-stack V2X framework for ns-3 covering ITS-G5, C-V2X, and LTE with SUMO and CARLA co-simulation; the continuation of ms-van3t.
* [Vanetza](https://github.com/riebl/vanetza) - Open-source ETSI C-ITS protocol stack covering GeoNetworking, BTP, DCC, and the security layer, widely used as the reference implementation for V2X experimentation.

## EV Charging Security

* [dsV2Gshark](https://github.com/dspace-group/dsV2Gshark) - Wireshark plugin that dissects ISO 15118 and DIN 70121 traffic, decoding EXI-encoded V2G payloads and SLAC handshakes into readable fields.
* [EVerest](https://github.com/EVerest/everest-core) - Linux Foundation Energy full-stack open-source EV charging firmware implementing OCPP 1.6/2.0.1/2.1, ISO 15118-2/-3/-20, IEC 61851, and DIN SPEC 70121, useful as a reference target and test peer.
* [open-plc-utils](https://github.com/qca/open-plc-utils) - Qualcomm Atheros powerline toolkit for HomePlug AV and Green PHY devices, the standard means of inspecting and manipulating the PLC layer that CCS charging sessions run over.
* [OpenV2G](https://github.com/Martin-P/OpenV2G) - C implementation of the ISO 15118 and DIN 70121 vehicle-to-grid interface with an EXI codec, widely reused as the encoding engine behind other V2G analysis tooling.
* [pyPLC](https://github.com/uhi22/pyPLC) - Python toolkit for CCS charging research that can pose as vehicle or charger, sniff HomePlug Green PHY traffic, and walk the SLAC, DIN 70121, and ISO 15118 state machines.
* [V2Gdecoder](https://github.com/FlUxIuS/V2Gdecoder) - Encodes and decodes EXI-compressed V2G messages on the fly, turning captured ISO 15118 exchanges into editable XML for replay and fuzzing.
* [WWCP_ISO15118](https://github.com/OpenChargingCloud/WWCP_ISO15118) - ISO 15118 implementation covering SLAC, SDP, V2GTP, -2 and -20, explicitly shipping attack vectors and penetration-testing workflows for the individual subprotocols.

## Hardware Interfaces

* [CANtact](https://github.com/linklayer/cantact-app) - Open-source hardware CAN interface and desktop app supporting live tracing, frame transmission, ISO-TP, JavaScript scripting, and candump-format traces.
* [panda](https://github.com/commaai/panda) - Open-source CAN and CAN FD interface firmware from comma.ai running on an STM32H725, with Python bindings for full read/write access to vehicle buses.
* [RAMN](https://github.com/ToyotaInfoTech/RAMN) - Resistant Automotive Miniature Network, a four-ECU CAN/CAN FD testbed on a single board with KiCad sources, CARLA closed-loop simulation, and use as the Car Hacking Village CTF platform.

## Security Analysis

* [Automotive Threat Modeling Template](https://github.com/nccgroup/The_Automotive_Threat_Modeling_Template) - NCC Group stencil set for the Microsoft Threat Modeling Tool, supplying vehicle-specific element types, trust boundaries, and threat rules for ECU and in-vehicle network diagrams.
* [AVCDL](https://github.com/nutonomy/AVCDL) - Motional's open-sourced Versatile Cybersecurity Development Lifecycle with process definitions and templates mapped to ISO/SAE 21434, ISO 24089, and UN R155/R156, assessed by TUV SUD.
* [QuickTARA](https://github.com/leonkalema/quicktara) - Professional-grade TARA (Threat Analysis and Risk Assessment) tool implementing STRIDE analysis and ISO 21434/UN R155 compliance.
* [Security AutoDesigner](https://plaxidityx.com/products/security-autodesigner/) - Automated TARA platform for creating ISO 21434 and UNR 155 compliant threat analysis reports.

## Penetration Testing

* [AutoFuze](https://github.com/DanAurea/AutoFuze) - Python toolkit for fuzzing and penetration testing ECUs over UDS, XCP, SOME/IP, and OBD, across CAN, DoIP, USB, and SPI transports.
* [automotive-security-research](https://github.com/ps1337/automotive-security-research) - Published reverse engineering results for two production vehicles including CAN matrices, extracted ECU security access keys, and UDS scanning proof-of-concepts.
* [Car Toolkit](https://github.com/j-schmied/car-toolkit) - Python-based toolkit for automotive penetration testing with CAN suite, CARAL, and virtual test bench setup.
* [DongleScope](https://github.com/OSUSecLab/DongleScope) - Automated tool for detecting vulnerabilities in wireless OBD-II dongles based on USENIX Security 2020 research.
* [PiCCANTE](https://github.com/Alia5/PiCCANTE) - Dirt-cheap CAN bus exploration tool built on Raspberry Pi Pico as an open-source hardware/software solution.
* [pwnobd](https://github.com/Nnubes256/pwnobd) - Offensive cybersecurity toolkit for vulnerability analysis of OBD-II devices presented at Black Hat Europe 2024.
* [SecOC Key Extractor](https://github.com/i-can-hack/secoc) - Scripts to extract SecOC (Secure On-Board Communication) keys from Toyota vehicles using comma.ai panda hardware.
* [tesla-opener](https://github.com/rgerganov/tesla-opener) - Open-source tool to open Tesla charging port using HackRF and WebUSB with ASK/OOK RF transmission.

## Datasets

* [CAN-MIRGU](https://github.com/sampathrajapaksha/CAN-MIRGU) - CAN bus attack dataset from a modern vehicle driven on real roads over six days, with physically verified masquerade, suspension, and real attacks.
* [Car Hacking Dataset](https://ocslab.hksecurity.net/Datasets/car-hacking-dataset) - HCRL captures from a Kia Soul with labelled DoS, fuzzing, and RPM and gear spoofing injections, the most widely cited baseline in CAN intrusion detection papers.
* [Cross-Vehicle Generalisation Benchmark](https://github.com/obaf/Cross-Vehicle-Generalisation-of-In-Vehicle-Intrusion-Detection) - Leave-one-vehicle-out benchmark unifying ROAD, CIDv2, and can-train-and-test into 217 captures across eight vehicles for evaluating whether CAN IDS models transfer.
* [ROAD](https://0xsam.com/road/) - Real ORNL Automotive Dynamometer CAN intrusion dataset with verified fuzzing, targeted ID, masquerade, and accelerator attacks captured on a dynamometer.
* [SynCAN](https://github.com/etas/SynCAN) - ETAS synthetic CAN benchmark with continuous, plateau, playback, suspension, and flooding attacks in the signal space, for comparing IDS that work on decoded signals rather than raw arbitration IDs.

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
* [Viden: Attacker Identification on In-Vehicle Networks](https://arxiv.org/abs/1708.08414) - Cho and Shin, ACM CCS 2017. Fingerprints transmitting ECUs by their analogue voltage signature, moving CAN defence from detecting an attack to naming the ECU responsible.
* [WALNUT: Waging Doubt on the Integrity of MEMS Accelerometers with Acoustic Injection Attacks](https://spqrlab1.github.io/papers/trippel-IEEE-oaklawn-walnut-2017.pdf) - Trippel, Weisse, Xu, Honeyman, and Fu, IEEE EuroS&P 2017. Acoustic resonance attacks that forge accelerometer output, establishing analogue sensor integrity as its own threat model.
* [VulCAN: Efficient Component Authentication and Software Isolation for Automotive Control Networks](https://vanbulck.net/files/acsac17-vulcan.pdf) - Van Bulck, Muhlberg, and Piessens, ACSAC 2017. Combines message authentication with trusted-computing isolation, defending against an adversary running arbitrary code on a participating ECU.
* [Illusion and Dazzle: Adversarial Optical Channel Exploits Against Lidars for Automotive Applications](https://eprint.iacr.org/2017/613) - Shin, Kim, Kwon, and Kim, CHES 2017. Saturates and spoofs an automotive LiDAR over its optical channel, creating fake points and blinding it entirely; the precursor to later LiDAR perception attacks.
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
* [CANflict: Exploiting Peripheral Conflicts for Data-Link Layer Attacks on Automotive Networks](https://arxiv.org/abs/2209.09557) - de Faveri Tron et al., ACM CCS 2022. Software-only data link layer attacks from a remotely compromised ECU, abusing peripheral pin conflicts to craft polyglot frames and break the protocol's own rules.
* [RollBack: A New Time-Agnostic Replay Attack Against the Automotive Remote Keyless Entry Systems](https://arxiv.org/abs/2210.11923) - Csikor et al., Black Hat USA 2022. Replaying already-invalid rolling codes in sequence triggers a resynchronisation rollback, unlocking a vehicle indefinitely and defeating the countermeasure that stopped RollJam.
* [Brokenwire: Wireless Disruption of CCS Electric Vehicle Charging](https://www.ndss-symposium.org/ndss-paper/brokenwire-wireless-disruption-of-ccs-electric-vehicle-charging/) - Kohler, Baker, Strohmeier, and Martinovic, NDSS 2023. Aborts CCS rapid-charging sessions wirelessly from tens of metres with off-the-shelf radio hardware, against individual vehicles or whole fleets.
* [SoK: Kicking CAN Down the Road. Systematizing CAN Security Knowledge](https://arxiv.org/abs/2510.02960) - Serag et al., 2025. Systematization of two decades of CAN security, with a unified taxonomy and assessment model for attackers, attacks, and defences.
* [Current Affairs: A Security Measurement Study of CCS EV Charging Deployments](https://www.usenix.org/conference/usenixsecurity25/presentation/szakaly) - Szakaly et al., USENIX Security 2025. First measurement of publicly deployed CCS DC chargers, finding that only 12 percent of 325 units across four European countries negotiated TLS and that most ran decade-old HomePlug modem firmware.

## Books

* [A Comprehensible Guide to Controller Area Network](https://copperhilltech.com/a-comprehensible-guide-to-controller-area-network/) - Wilfried Voss, Copperhill 2005. The standard plain-language reference on CAN itself, covering frame formats, arbitration, error handling, and timing that vehicle network attacks depend on.
* [Automotive Cyber Security](https://books.google.com/books?id=uTD_DwAAQBAJ) - Shiho Kim and Rakesh Shrestha, Springer 2020. Academic introduction to connected and autonomous vehicle security, threats, and the standardisation landscape.
* [Automotive Cybersecurity Engineering Handbook](https://books.google.com/books/about/Automotive_Cybersecurity_Engineering_Han.html?id=UK_YEAAAQBAJ) - Ahmad MK Nasser, Packt 2023. Practitioner's guide to building cyber-resilient vehicles, covering threat analysis, hardware security, and ISO/SAE 21434 engineering practice.
* [Building Secure Cars](https://www.wiley.com/en-us/Building+Secure+Cars:+Assuring+the+Automotive+Software+Development+Lifecycle-p-9781119710745) - Dennis Kengo Oka, Wiley 2021. Focuses on assuring the automotive software development lifecycle, from secure coding and static analysis through fuzzing and penetration testing.
* [Cybersecurity for Commercial Vehicles](https://books.google.com/books?id=R3h0EAAAQBAJ) - Gloria D'Anna, SAE International 2018. Covers heavy vehicle and fleet security, how it differs from passenger cars, SAE J3061, platooning, and breach forensics.
* [Hacking Connected Cars](https://www.wiley.com/en-us/-p-9781119491804) - Alissa Knight, Wiley 2020. Tactics, techniques, and procedures for penetration testing, threat modelling, and risk assessment of telematics control units and infotainment systems.
* [Offensive Automotive Cybersecurity](https://books.google.com/books/about/Offensive_Automotive_Cybersecurity.html?id=tQbfEQAAQBAJ) - Ahmad MK Nasser and Dennis Kengo Oka, Packt 2026. The two handbook authors together on the offensive side, covering exploitation of modern automotive platforms.
* [The Car Hacker's Handbook](https://www.opengarages.org/handbook/) - Craig Smith, No Starch Press 2016. The foundational practical guide to vehicle security, covering threat modelling, CAN reverse engineering, and ECU exploitation; free to read online via Open Garages.

## Learning Resources

* [Automotive Cybersecurity Roadmap](https://github.com/AutoSecurityy/Automotive-Cybersecurity-Roadmap) - Structured learning path from CAN and UDS fundamentals through TARA, firmware reverse engineering, and hardware hacking into specialized career tracks.
* [Automotive Security Timeline](https://github.com/automotive-security/Automotive-Security-Timeline) - Continuously updated knowledge base of automotive cybersecurity events including vulnerability disclosures, attack demonstrations, Pwn2Own Automotive results, and supply-chain incidents.
* [Automotive-Networking-Security](https://automotive-network-security.com/standard_solutions.shtml) - Automotive networking security standards and solutions overview.
* [Car Hacking Village](https://www.carhackingvillage.com/events) - Non-profit running hands-on car hacking workshops and CTFs at DEF CON, Black Hat, HITCON, CODE BLUE, and other conferences.
* [OpenGarages](https://www.opengarages.org/) - Open vehicle research collective behind the Car Hacker's Handbook, publishing the free edition of the book, ICSim, and workshop material for hands-on vehicle security practice.
* [What is Automotive MACsec?](https://youtu.be/5QiHmMoJCOE) - Video training on Automotive MACsec concepts by Technica Engineering.

## Related Awesome Lists

* [Awesome CANb IDs](https://github.com/iDoka/awesome-automotive-can-id) - CAN bus ID reference and documentation.
* [Awesome CANbus](https://github.com/iDoka/awesome-canbus) - Comprehensive CAN bus security resources.
* [Awesome Connected Things Sec](https://github.com/V33RU/awesome-connected-things-sec) - Security resources across IoT, embedded, industrial, and automotive systems with a dedicated automotive section.
* [Awesome Embedded Security](https://github.com/hexsecs/awesome-embedded-security) - Tools and knowledge for embedded security research.
* [Awesome EV Charging](https://github.com/juherr/awesome-ev-charging) - Curated specifications, tools, and resources for EV charging protocols including OCPP, ISO 15118, OCPI, and Eichrecht.
* [Awesome Vehicle Security](https://github.com/jaredthecoder/awesome-vehicle-security) - Long-running curated list of vehicle security resources, hardware, software, researchers, and manufacturer disclosure programs.
