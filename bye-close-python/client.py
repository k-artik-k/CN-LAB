import socket

def main():
    try:
        # Establish connection to the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 1010))

        while True:
            # Read user input
            message = input("You: ")

            # Send message to the server
            s.sendall(message.encode())

            # If the message is "bye", exit the loop
            if message.lower() == "bye":
                break

            # Receive response from the server
            response = s.recv(1024).decode()
            print("SERVER:", response)

        # Close the connection
        s.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
