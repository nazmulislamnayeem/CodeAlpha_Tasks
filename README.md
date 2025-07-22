This project is a **Python-based real-time network sniffer** built using the `scapy` library. It captures and analyzes live packets from the network, extracting:

- Source and destination IP addresses
- Protocol type and number (TCP, UDP, ICMP, ARP)
- Raw payloads (decoded safely or shown in hex)
  
---
## 🔍 Features

- Real-time packet capture
- Supports TCP, UDP, ICMP, and ARP
- Displays:
  - Protocol Name and Number
  - Source & Destination IPs
  - Payload (safely decoded or hex)
- Cross-platform (tested on **Windows 11 with Scapy**)

---

## 🛠️ How to Run

1. Install required library: pip install scapy
2. Run script as administrator (for packet capture permission): python NetworkSniffer.py
3. Output example: Protocol: TCP (#6) | Src: 192.168.0.105 -> Dst: 172.217.166.174 | Payload: GET / HTTP/1.1

---

## 👨‍💻 Author
**Nazmul Islam Nayeem**  
Cyber Security Intern @CodeAlpha  
📧 [nazmulislamnayeem03@gmail.com](mailto:nazmulislamnayeem03@gmail.com)  
🔗 [LinkedIn :- https://www.linkedin.com/in/nazmulin12035/]
