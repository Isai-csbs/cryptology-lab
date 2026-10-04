import time
import random

# ============================================================
# IPTABLES FIREWALL SIMULATION USING PYTHON
# No external packages required
# ============================================================

print("=" * 65)
print("             IPTABLES FIREWALL SIMULATION")
print("=" * 65)

# ------------------------------------------------------------
# 1. SYSTEM INFORMATION
# ------------------------------------------------------------

print("\n[1] OPENING LINUX / WSL ENVIRONMENT")
time.sleep(1)

print("Linux terminal started successfully.")
print("User@Linux:~$")

# ------------------------------------------------------------
# 2. INSTALL IPTABLES
# ------------------------------------------------------------

print("\n[2] INSTALLING IPTABLES")
time.sleep(1)

print("$ sudo apt update")
print("Package repository updated successfully.")

time.sleep(1)

print("$ sudo apt install iptables -y")
print("iptables installed successfully.")

time.sleep(1)

print("$ sudo iptables --version")
print("iptables v1.8.9")

# ------------------------------------------------------------
# 3. VIEW EXISTING FIREWALL RULES
# ------------------------------------------------------------

print("\n[3] EXISTING FIREWALL RULES")
print("-" * 65)

print("$ sudo iptables -L -v -n")
print()
print("Chain INPUT (policy ACCEPT)")
print("target     prot  source          destination")
print()
print("Chain FORWARD (policy ACCEPT)")
print("target     prot  source          destination")
print()
print("Chain OUTPUT (policy ACCEPT)")
print("target     prot  source          destination")

# ------------------------------------------------------------
# 4. FLUSH EXISTING RULES
# ------------------------------------------------------------

print("\n[4] FLUSHING EXISTING FIREWALL RULES")
time.sleep(1)

print("$ sudo iptables -F")
print("$ sudo iptables -X")

print("Existing firewall rules cleared successfully.")

# ------------------------------------------------------------
# 5. CREATE FIREWALL RULES
# ------------------------------------------------------------

print("\n[5] CONFIGURING FIREWALL RULES")
print("-" * 65)

rules = []

# Loopback
rules.append({
    "target": "ACCEPT",
    "protocol": "all",
    "port": "lo",
    "description": "Allow loopback traffic"
})

print("1. Allowing loopback traffic...")
print("   sudo iptables -A INPUT -i lo -j ACCEPT")

# Established connections
rules.append({
    "target": "ACCEPT",
    "protocol": "all",
    "port": "ESTABLISHED",
    "description": "Allow established and related connections"
})

print("2. Allowing established and related connections...")
print("   sudo iptables -A INPUT -m conntrack")
print("   --ctstate RELATED,ESTABLISHED -j ACCEPT")

# SSH
rules.append({
    "target": "ACCEPT",
    "protocol": "tcp",
    "port": "22",
    "description": "Allow SSH"
})

print("3. Allowing SSH port 22...")
print("   sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")

# HTTP
rules.append({
    "target": "ACCEPT",
    "protocol": "tcp",
    "port": "80",
    "description": "Allow HTTP"
})

print("4. Allowing HTTP port 80...")
print("   sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT")

# Test port 8080
rules.append({
    "target": "ACCEPT",
    "protocol": "tcp",
    "port": "8080",
    "description": "Allow test port 8080"
})

print("5. Allowing test port 8080...")
print("   sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT")

# Test port 9090
rules.append({
    "target": "DROP",
    "protocol": "tcp",
    "port": "9090",
    "description": "Block test port 9090"
})

print("6. Blocking test port 9090...")
print("   sudo iptables -A INPUT -p tcp --dport 9090 -j DROP")

# ------------------------------------------------------------
# 6. DEFAULT FIREWALL POLICIES
# ------------------------------------------------------------

print("\n[6] SETTING DEFAULT FIREWALL POLICIES")
print("-" * 65)

print("$ sudo iptables -P INPUT DROP")
print("$ sudo iptables -P FORWARD DROP")
print("$ sudo iptables -P OUTPUT ACCEPT")

print("\nDefault policies configured:")
print("INPUT   : DROP")
print("FORWARD : DROP")
print("OUTPUT  : ACCEPT")

# ------------------------------------------------------------
# 7. DISPLAY FIREWALL RULES
# ------------------------------------------------------------

print("\n[7] FIREWALL CONFIGURATION")
print("-" * 65)

print("Chain INPUT (policy DROP)")
print("target     prot      destination")
print("ACCEPT     all       loopback")
print("ACCEPT     all       established")
print("ACCEPT     tcp       tcp dpt:22")
print("ACCEPT     tcp       tcp dpt:80")
print("ACCEPT     tcp       tcp dpt:8080")
print("DROP       tcp       tcp dpt:9090")

# ------------------------------------------------------------
# 8. TEST PORT 8080
# ------------------------------------------------------------

print("\n[8] TESTING PORT 8080")
print("-" * 65)

print("Starting test service on port 8080...")
time.sleep(1)

print("Serving HTTP on 0.0.0.0 port 8080 ...")

time.sleep(1)

print("\nTesting connection to port 8080...")
print("Request: HTTP GET /")

time.sleep(1)

print("\nHTTP/1.1 200 OK")
print("Content-Type: text/html")
print("Connection: successful")

print("\nFirewall decision:")
print("TCP")
print("  |")
print("Port 8080")
print("  |")
print("iptables")
print("  |")
print("ACCEPT")
print("  |")
print("Connection ALLOWED")

# ------------------------------------------------------------
# 9. TEST PORT 9090
# ------------------------------------------------------------

print("\n[9] TESTING PORT 9090")
print("-" * 65)

print("Starting test service on port 9090...")
time.sleep(1)

print("Serving HTTP on 0.0.0.0 port 9090 ...")

time.sleep(1)

print("\nTesting incoming connection to port 9090...")
print("TCP connection request received.")

time.sleep(1)

print("\nFirewall decision:")
print("TCP")
print("  |")
print("Port 9090")
print("  |")
print("iptables")
print("  |")
print("DROP")
print("  |")
print("Connection BLOCKED")

# ------------------------------------------------------------
# 10. PACKET COUNTERS
# ------------------------------------------------------------

print("\n[10] FIREWALL PACKET COUNTERS")
print("-" * 65)

accepted_packets = random.randint(3, 8)
accepted_bytes = accepted_packets * 60

dropped_packets = random.randint(2, 5)
dropped_bytes = dropped_packets * 60

print("pkts     bytes     target    protocol    destination")
print(
    "{}        {}       ACCEPT    tcp         tcp dpt:8080".format(
        accepted_packets,
        accepted_bytes
    )
)

print(
    "{}        {}       DROP      tcp         tcp dpt:9090".format(
        dropped_packets,
        dropped_bytes
    )
)

# ------------------------------------------------------------
# 11. FINAL VERIFICATION
# ------------------------------------------------------------

print("\n[11] FINAL FIREWALL VERIFICATION")
print("-" * 65)

print("$ sudo iptables -L INPUT -v -n")
print()
print("Chain INPUT (policy DROP)")
print()
print("ACCEPT  all    loopback")
print("ACCEPT  all    established,related")
print("ACCEPT  tcp    tcp dpt:22")
print("ACCEPT  tcp    tcp dpt:80")
print("ACCEPT  tcp    tcp dpt:8080")
print("DROP    tcp    tcp dpt:9090")

# ------------------------------------------------------------
# 12. SECURITY SUMMARY
# ------------------------------------------------------------

print("\n[12] FIREWALL SECURITY SUMMARY")
print("-" * 65)

print("Authorized traffic:")
print("  Port 22   -> ACCEPT")
print("  Port 80   -> ACCEPT")
print("  Port 8080 -> ACCEPT")

print("\nBlocked traffic:")
print("  Port 9090 -> DROP")
print("  Other unapproved incoming traffic -> DROP")

print("\nOutgoing traffic:")
print("  OUTPUT -> ACCEPT")

# ------------------------------------------------------------
# 13. FINAL RESULT
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                         RESULT")
print("=" * 65)

print("The iptables firewall demonstration was completed successfully.")
print()
print("The program demonstrated:")
print("1. Firewall rule configuration")
print("2. Loopback traffic permission")
print("3. Established connection permission")
print("4. SSH port 22 permission")
print("5. HTTP port 80 permission")
print("6. Test port 8080 ACCEPT rule")
print("7. Test port 9090 DROP rule")
print("8. Default INPUT DROP policy")
print("9. Default FORWARD DROP policy")
print("10. OUTPUT ACCEPT policy")
print("11. Packet and byte counters")
print("12. Firewall traffic filtering")

print("\nPort 8080 : CONNECTION ALLOWED")
print("Port 9090 : CONNECTION BLOCKED")

print("\nTherefore, packet filtering and access-control")
print("capabilities of an iptables firewall were demonstrated.")

print("=" * 65)

input("\nPress Enter to exit...")
