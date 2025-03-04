import socket

def request_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 59)

    # Send the file name request to the server
    client_socket.sendto(file_name.encode(), server_address)
    
    with open(f"received_{file_name}", "wb") as file:
        while True:
            data, _ = client_socket.recvfrom(1024)
            if not data:
                break
            file.write(data)
    print(f"File '{file_name}' received.")
    
    # Wait for the server to send the success message
    data, _ = client_socket.recvfrom(1024)
    print(data.decode())  # Print the 'File received successfully' message

if __name__ == "__main__":
    file_name = input("Enter the file name to request: ")
    request_file(file_name)
