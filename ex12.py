import socket
import threading
import time

HOST = "127.0.0.1"
MITM_PORT = 8000
SERVER_PORT = 9000


# ---------------- SERVER ----------------
def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, SERVER_PORT))
    s.listen(1)

    print("Test Server started on port 9000")
    print("Waiting for MITM relay...")

    conn, address = s.accept()
    print("Connection received from:", address)

    data = conn.recv(1024)
    message = data.decode()

    print("Message received at Server:", message)

    reply = "Hello Client, message received by Server"
    conn.send(reply.encode())

    conn.close()
    s.close()

    print("Server stopped.")


# ---------------- MITM RELAY ----------------
def mitm():
    m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    m.bind((HOST, MITM_PORT))
    m.listen(1)

    print("\nMITM Relay started on port 8000")
    print("Waiting for Client...")

    client_conn, client_address = m.accept()

    print("\nClient connected:", client_address)

    client_data = client_conn.recv(1024)
    client_message = client_data.decode()

    print("\nMITM observed Client message:")
    print(client_message)

    # Connect MITM to Server
    server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_conn.connect((HOST, SERVER_PORT))

    # Forward message to server
    server_conn.send(client_data)

    print("\nMessage forwarded to Server")

    # Receive server reply
    server_reply = server_conn.recv(1024)

    print("\nMITM observed Server reply:")
    print(server_reply.decode())

    # Forward reply to client
    client_conn.send(server_reply)

    print("\nReply forwarded to Client")

    server_conn.close()
    client_conn.close()
    m.close()

    print("\nMITM Relay stopped.")


# ---------------- CLIENT ----------------
def client():
    time.sleep(1)

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, MITM_PORT))

    message = input("\nEnter message: ")

    c.send(message.encode())

    reply = c.recv(1024)

    print("\nReply from Server:", reply.decode())

    c.close()


# ---------------- MAIN PROGRAM ----------------
print("==============================================")
print("   MAN-IN-THE-MIDDLE SOCKET DEMONSTRATION")
print("==============================================")

# Start Server
server_thread = threading.Thread(target=server)
server_thread.start()

time.sleep(1)

# Start MITM
mitm_thread = threading.Thread(target=mitm)
mitm_thread.start()

time.sleep(1)

# Start Client
client_thread = threading.Thread(target=client)
client_thread.start()

# Wait for all threads
client_thread.join()
mitm_thread.join()
server_thread.join()

print("\n==============================================")
print("              EXPERIMENT COMPLETED")
print("==============================================")
print("The MITM relay observed and forwarded")
print("the unencrypted client-server communication.")
