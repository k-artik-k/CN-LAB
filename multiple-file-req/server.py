import socket
import os
import threading

PORT = 55

# Function to handle client requests
def handle_client(client_socket, addr):
    print(f"Client connected from {addr}")

    # Receive file request
    file_name = client_socket.recv(1024).decode()
    print(f"Client requested: {file_name}")

    # Check and send the file if it exists
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            while (chunk := file.read(1024)):
                client_socket.sendall(chunk)
        print("File sent successfully.")
    else:
        print("File not found.")
        client_socket.sendall("File not found.".encode())

    client_socket.close()

def main():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", PORT))
    server_socket.listen(5)
    print(f"Server listening on port {PORT}...")

    try:
        while True:
            # Accept a new client connection
            client_socket, addr = server_socket.accept()
            # Handle each client in a new thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
