# IoT-Driven Cisco Network Failover Automation

## Overview
This project demonstrates an **Industrial IoT (IIoT)** solution where a simulated temperature sensor triggers automatic network failover on a Cisco Catalyst 8000v router. Built using Python and Netmiko, it showcases the intersection of IoT sensing and enterprise networking automation.

## The Problem It Solves
In a factory, if a server rack overheats, the network switch might fail. Instead of waiting for an IT engineer to manually SSH in, this script detects the temperature and proactively reroutes traffic, reducing downtime from minutes to milliseconds.

## Technologies Used
- **Python** (Netmiko library)
- **Cisco IOS XE** (Catalyst 8000v)
- **Cisco DevNet Sandbox** (Cloud-based lab environment)
- **SSH / Automation**

## How It Works
1. The Python script generates simulated temperature readings.
2. If the temperature exceeds 75°C, the script automatically logs into the Cisco router via SSH.
3. It modifies `Loopback1` interface descriptions to indicate a "Failover Active" state.
4. When the temperature drops below 70°C, it restores the "Normal" state.

## Live Proof
![Screenshot 1](screenshot1.png)
*Screenshot showing the Python script triggering the router change.*

![Screenshot 2](screenshot2.png)
*Screenshot showing the live router terminal updating the interface description.*

## Future Enhancements
- Integrate real sensor hardware (ESP32/Raspberry Pi).
- Replace Loopback logic with actual `shutdown`/`no shutdown` on primary interfaces.
- Add MQTT or AWS IoT Core for cloud integration.

## Author
[Your Name] - Fresh Graduate Computer Engineer, IoT Specialization, CCNA Certified.
