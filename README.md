## 🛠️ NETWORK SNIFFER(Python + Scapy)


This project is a **Python-based real-time network sniffer** built using the `scapy` library. It captures and analyzes live packets from the network, extracting:

## 🔍 Features

- Real-time packet capture
- Supports TCP, UDP, ICMP, and ARP
- Displays:
  - Protocol Name and Number
  - Source & Destination IPs
  - Payload (safely decoded or hex)
- Cross-platform (tested on **Windows 11 with Scapy**)

---
##🐍 Requirements

Python 3.6+

Scapy

Npcap (on Windows)  


## INSTALLATION:

Python: https://www.python.org/downloads/

Npcap (required for Scapy on Windows): https://npcap.com/#download

Install Scapy Library: pip install scapy

## For Linux: 

sudo apt install python3 -y

sudo apt install python3-pip -y

pip3 install scapy

nano NetworkSniffer.py (Copy NetworkSniffer.py code and paste Inside nano....)


## 🛠️ How to Run

1. Run cmd as administrator :  python NetworkSniffer.py (copy &  Paste the Python Code in VS CODE and ctrl + S)
   
2. sudo python3 NetworkSniffer.py( For Linux, Scapy needs root access for run )

3. Output example: Protocol: TCP (#6) | Src: 192.168.0.105 -> Dst: 172.217.166.174 | Payload: GET / HTTP/1.1
