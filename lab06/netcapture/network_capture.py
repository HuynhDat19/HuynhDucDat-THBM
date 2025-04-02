import subprocess
from scapy.all import *

def get_interfaces():
    resultn= subprocess.run(["netsh", "interface", "show","interface"], capture_output=True, text=True)
    output_lines = resultn.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) >=4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured packet:")
        print(str(packet))

interfaces = get_interfaces()

print("Available network interfaces:")
for i, iface in enumerate(interfaces, start = 1):
    print(f"{i}. {iface}")

choice = int(input("Select an interface to capture packets: "))
selected_iface  = interfaces[choice - 1]

sniff(iface=selected_iface, prn=packet_handler, filter="tcp")



        