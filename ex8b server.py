import socket

HOST = "127.0.0.1"
PORT = 8888

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to honeypot
client.connect((HOST, PORT))

# Receive welcome message
message = client.recv(1024)

print(message.decode())

# Get input from user
user_message = input("Type Message: ")

# Send message
client.send(user_message.encode())

# Receive server response
response = client.recv(1024)

print(response.decode())

# Close connection
client.close()
