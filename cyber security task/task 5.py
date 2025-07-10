from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import datetime

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "Unknown"

        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
        elif packet.haslayer(ICMP):
            proto = "ICMP"

        print("\n--- Packet Captured ---")
        print(f"Time      : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Source IP : {ip_src}")
        print(f"Dest IP   : {ip_dst}")
        print(f"Protocol  : {proto}")

        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load.decode(errors="replace")
                print(f"Payload   : {payload[:100]}")  # Truncate to 100 characters
            except Exception as e:
                print("Payload   : <Unable to decode>")

print("🔍 Starting Packet Sniffer (press Ctrl+C to stop)...")
# Start sniffing (store=0 avoids memory overload, count=0 = infinite packets)
sniff(prn=packet_callback, store=0)
