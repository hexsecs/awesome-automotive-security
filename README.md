# Awesome Automotive Security [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A curated Awesome-list for automotive security tools and knowledge. If other better lists exist, we'll try to reference them instead of duplicating work.

## Table of Contents

* [CAN Bus Analysis](#can-bus-analysis)
* [Diagnostic Tools](#diagnostic-tools)
* [Automotive Ethernet](#automotive-ethernet)
* [RF and Key Fob Analysis](#rf-and-key-fob-analysis)
* [Infotainment and IVI](#infotainment-and-ivi)
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

## Diagnostic Tools

* [UDSim](https://github.com/zombieCraig/UDSim) - UDS (Unified Diagnostic Services) ECU simulator and fuzzer for discovering and testing UDS services.
* [VW_Flash](https://github.com/bri3d/VW_Flash) - Flashing tools for VW AG control units over UDS supporting Simos18.1/6/10 and DQ250-MQB.
* [conescan](https://github.com/ConnorRigby/conescan) - Automotive ECU hacking supertool for firmware dumping and manipulation via J2534 OBD interfaces.
* [uds-firmware-extraction](https://github.com/honinb0n/uds-firmware-extraction) - Tool for extracting ECU firmware from UDS flash traffic following ISO-14229 standard.

## Automotive Ethernet

* [ICS CAP](https://intrepidcs.com/products/software/ics-cap/) - Free Wireshark plugin for monitoring Automotive Ethernet, CAN, CAN FD, LIN, and FlexRay networks.
* [eth-ws-someip](https://github.com/jamores/eth-ws-someip) - Wireshark LUA dissectors for Automotive Ethernet SOME/IP and SOME/IP-SD protocols (Autosar 4.2).

## RF and Key Fob Analysis

* [KeyFob Analysis Toolkit (KAT)](https://github.com/KaraZajac/KAT) - Toolkit for analyzing, decoding, and retransmitting key fob signals with support for HackRF, RTL-SDR, and Flipper Zero.
* [Universal Radio Hacker (URH)](https://github.com/miek/urh) - Open-source suite for wireless protocol investigation with native SDR support and easy signal demodulation.

## Infotainment and IVI

* [ic1101](https://github.com/librick/ic1101) - Open research project for reverse engineering 10th generation Honda Civic infotainment systems (Android-based, NVIDIA Tegra 3).
* [Chimaera](https://link.springer.com/article/10.1007/s11416-024-00522-4) - Research framework for IVI (In-Vehicle Infotainment) firmware reverse engineering and exploitation targeting Hyundai/Kia Gen5W_L systems.

## Security Analysis

* [QuickTARA](https://github.com/leonkalema/quicktara) - Professional-grade TARA (Threat Analysis and Risk Assessment) tool implementing STRIDE analysis and ISO 21434/UN R155 compliance.
* [Security AutoDesigner](https://plaxidityx.com/products/security-autodesigner/) - Automated TARA platform for creating ISO 21434 and UNR 155 compliant threat analysis reports.

## Penetration Testing

* [Car Toolkit](https://github.com/j-schmied/car-toolkit) - Python-based toolkit for automotive penetration testing with CAN suite, CARAL, and virtual test bench setup.
* [PiCCANTE](https://github.com/Alia5/PiCCANTE) - Dirt-cheap CAN bus exploration tool built on Raspberry Pi Pico as an open-source hardware/software solution.

## Learning Resources

* [Automotive Security Timeline](https://github.com/delikely/Automotive-Security-Timeline) - Timeline of automotive security research and vulnerabilities.
* [Automotive-Networking-Security](https://automotive-network-security.com/standard_solutions.shtml) - Automotive networking security standards and solutions overview.
* [What is Automotive MACsec?](https://youtu.be/5QiHmMoJCOE) - Video training on Automotive MACsec concepts by Technica Engineering.

## Related Awesome Lists

* [Awesome CANbus](https://github.com/iDoka/awesome-canbus) - Comprehensive CAN bus security resources.
* [Awesome CANb IDs](https://github.com/iDoka/awesome-automotive-can-id) - CAN bus ID reference and documentation.
