import socket
import os

PORT = 55

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", PORT))
server_socket.listen(1)
print(f"Server listening on port {PORT}...")

client_socket, addr = server_socket.accept()
print(f"Client connected from {addr}")

# Receive file request
file_name = client_socket.recv(1024).decode()
print(f"Client requested: {file_name}")

# Check and send file
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        client_socket.sendall(file.read())
    print("File sent successfully.")
else:
    print("File not found.")

client_socket.close()
server_socket.close()
