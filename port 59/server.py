import socket
import threading

def handle_client(client_socket, client_address):
    file_name, _ = client_socket.recvfrom(1024)
    try:
        with open(file_name.decode(), 'rb') as file:
            while chunk := file.read(1024):
                client_socket.sendto(chunk, client_address)
        # After sending the file, send a success message
        client_socket.sendto(b"File received successfully", client_address)
    except FileNotFoundError:
        client_socket.sendto(b"File not found", client_address)

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 59))
    print("Server listening on port 59...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        threading.Thread(target=handle_client, args=(server_socket, client_address)).start()

if __name__ == "__main__":
    run_server()
