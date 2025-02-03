import socket

def main():
    server_address = "localhost"
    port = 55

    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, port))
        print(f"Connected to server at {server_address}:{port}")

        # Get file name from user
        file_name = input("Enter the name of the file to request: ")

        # Send file request to server
        client_socket.sendall(file_name.encode())

        # Prepare to receive the file
        with open(f"Received_{file_name}", "wb") as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break  # Stop when no more data is received
                file.write(data)

        print(f"File received & saved as 'Received_{file_name}'.")

    except Exception as e:
        print("Error:", e)
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
