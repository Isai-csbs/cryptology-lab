import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 8888

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind host and port
server.bind((HOST, PORT))

# Start listening
server.listen(5)

print("====================================")
print("      SIMPLE PYTHON HONEYPOT")
print("====================================")
print("Honeypot started on port", PORT)
print("Waiting for connections...")

while True:

    # Accept connection
    client, address = server.accept()

    print("\n[+] Connection Detected")
    print("IP Address :", address[0])
    print("Port       :", address[1])
    print("Time       :", datetime.now())

    # Send message to client
    client.send(b"Welcome to Test Server\nEnter a message: ")

    # Receive message
    data = client.recv(1024)

    # Convert bytes to text
    message = data.decode().strip()

    print("Message :", message)

    # Send response
    client.send(b"Message received\n")

    # Close connection
    client.close()

    print("[+] Connection Closed")
    print("------------------------------------")
