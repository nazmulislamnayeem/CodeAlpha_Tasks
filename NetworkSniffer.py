from scapy.all import sniff, IP, ARP, Raw
import string

protocol_map = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}

def is_printable(s):
    return all(chr(c) in string.printable for c in s)

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto_num = ip_layer.proto
        proto_name = protocol_map.get(proto_num, f"Unknown ({proto_num})")
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        if packet.haslayer(Raw):
            raw_data = bytes(packet[Raw].load)
            if is_printable(raw_data):
                payload = raw_data.decode('utf-8', errors='replace')
            else:
                payload = raw_data.hex()[:60] + "..." 
        else:
            payload = "<No Payload>"

        print(f"Protocol: {proto_name} (#{proto_num}) | Src: {src_ip} -> Dst: {dst_ip} | Payload: {payload}")

    elif packet.haslayer(ARP):
        arp_layer = packet[ARP]
        print(f"Protocol: ARP | Src: {arp_layer.psrc} -> Dst: {arp_layer.pdst} | Payload: <No Payload>")

    else:
        print("Protocol: Unknown | Src/Dst: N/A | Payload: N/A")

print("[*] Sniffing started... Press Ctrl + C to stop.")
sniff(prn=process_packet)
