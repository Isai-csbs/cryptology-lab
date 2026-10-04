import time
import random

print("=" * 60)
print("           SNORT IDS SIMULATION USING PYTHON")
print("=" * 60)

# ---------------------------------------------------------
# 1. VERIFY SNORT INSTALLATION
# ---------------------------------------------------------

print("\n[1] VERIFY SNORT INSTALLATION")
time.sleep(1)

print("Snort Version: 2.9.20")
print("Snort installation verified successfully.")

# ---------------------------------------------------------
# 2. IDENTIFY NETWORK INTERFACE
# ---------------------------------------------------------

print("\n[2] IDENTIFY NETWORK INTERFACE")
time.sleep(1)

print("Available Network Interfaces:")
print("1. Ethernet")
print("2. Wi-Fi")
print("3. Loopback")

interface = input("Enter interface number to monitor: ")

print("Selected Interface:", interface)

# ---------------------------------------------------------
# 3. BASIC SNIFFER MODE
# ---------------------------------------------------------

print("\n[3] BASIC SNIFFER MODE")
time.sleep(1)

print("Capturing network packets...")
print("-" * 60)

packets = [
    "TCP 192.168.1.10:50432 -> 142.250.195.14:443",
    "UDP 192.168.1.10:53241 -> 8.8.8.8:53",
    "TCP 192.168.1.10:50120 -> 142.250.72.14:443",
    "ICMP 192.168.1.10 -> 8.8.8.8",
    "UDP 192.168.1.10:53001 -> 8.8.8.8:53"
]

for packet in packets:
    print(packet)
    time.sleep(0.5)

print("\nSnort processed", len(packets), "packets.")

# ---------------------------------------------------------
# 4. DISPLAY PACKET HEADER AND PAYLOAD
# ---------------------------------------------------------

print("\n[4] PACKET HEADER AND PAYLOAD")
time.sleep(1)

print("-" * 60)
print("Source      : 192.168.1.10:53120")
print("Destination : 8.8.8.8:53")
print("Protocol    : UDP")
print("TTL         : 128")
print("TOS         : 0x0")
print("Packet Data : example packet data")

# ---------------------------------------------------------
# 5. DISPLAY HEXADECIMAL AND ASCII DATA
# ---------------------------------------------------------

print("\n[5] HEXADECIMAL AND ASCII PACKET DATA")
time.sleep(1)

print("-" * 60)
print("45 00 00 3C 1C 46 40 00")
print("80 01 A6 EC C0 A8 01 0A")
print("08 08 08 08 08 00 4D 5C")
print("ASCII: E..<.F@........")

# ---------------------------------------------------------
# 6. PACKET LOGGING
# ---------------------------------------------------------

print("\n[6] PACKET LOGGING")
time.sleep(1)

print("Creating log directory...")
print("Packet information stored in log directory.")
print("Packet logging completed successfully.")

# ---------------------------------------------------------
# 7. CONFIGURE ICMP DETECTION RULE
# ---------------------------------------------------------

print("\n[7] CONFIGURE ICMP DETECTION RULE")
time.sleep(1)

rule = 'alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)'

print("Rule:")
print(rule)

print("\nRule Components:")
print("alert    - Generate an alert")
print("icmp     - Monitor ICMP packets")
print("any any  - Any source IP and port")
print("->       - Direction of traffic")
print("any any  - Any destination IP and port")
print("msg      - Alert message")
print("sid      - Unique signature ID")
print("rev      - Rule revision number")

# ---------------------------------------------------------
# 8. START SNORT IDS
# ---------------------------------------------------------

print("\n[8] START SNORT IDS")
time.sleep(1)

print("Snort IDS is monitoring interface", interface)

# ---------------------------------------------------------
# 9. GENERATE TEST ICMP TRAFFIC
# ---------------------------------------------------------

print("\n[9] GENERATE TEST ICMP TRAFFIC")
time.sleep(1)

print("Pinging 8.8.8.8 with 32 bytes of data:")

for count in range(4):
    delay = random.randint(15, 30)

    print(
        "Reply from 8.8.8.8: bytes=32 time={}ms TTL=117".format(delay)
    )

    time.sleep(0.5)

# ---------------------------------------------------------
# 10. IDS ALERT
# ---------------------------------------------------------

print("\n[10] IDS ALERT")
print("-" * 60)

time.sleep(1)

for count in range(4):
    print("[**] [1:1000001:1] ICMP Ping Detected [**]")
    time.sleep(0.5)

# ---------------------------------------------------------
# 11. DETECTION PROCESS
# ---------------------------------------------------------

print("\n[11] DETECTION PROCESS")
print("-" * 60)

print("PING 8.8.8.8")
print("     |")
print("     v")
print("ICMP Packet Generated")
print("     |")
print("     v")
print("Network Interface")
print("     |")
print("     v")
print("SNORT IDS")
print("     |")
print("     v")
print("ICMP Rule Matches")
print("     |")
print("     v")
print("ALERT GENERATED")
print("     |")
print("     v")
print('"ICMP Ping Detected"')

# ---------------------------------------------------------
# 12. RESULT
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("                         RESULT")
print("=" * 60)

print("The Snort IDS demonstration was completed successfully.")
print("Network packets were simulated and analyzed.")
print("Packet headers and payload data were displayed.")
print("Hexadecimal and ASCII packet data were displayed.")
print("An ICMP detection rule was applied.")
print("The ICMP detection alert was generated successfully.")

print("=" * 60)

input("\nPress Enter to exit...")
