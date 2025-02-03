import socket

def main():
    try:
        # Create a server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 1010))
        server_socket.listen(1)
        print("Server is listening on port 1010...")

        # Accept client connection
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        while True:
            # Receive message from the client
            client_message = client_socket.recv(1024).decode()
            print("CLIENT:", client_message)

            # If client sends "bye", terminate the connection
            if client_message.lower() == "bye":
                break

            # Get server response and send back
            server_response = input("You: ")
            client_socket.sendall(server_response.encode())

        # Close connections
        client_socket.close()
        server_socket.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
