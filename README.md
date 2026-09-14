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
* [Atlas](https://github.com/atlas-tuning/atlas) - Open-source ECU calibration application for Subaru and Toyota with Ghidra integration for firmware analysis.
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
