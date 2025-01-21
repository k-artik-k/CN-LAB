import socket
def start_server():
   server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   server_address = ('',53)
   server_socket.bind(server_address)
   server_socket.listen(1)
   print("server listening on port 53")
   while True:
      connection,client_address = server_socket.accept()
      try:
         print("Connection established with",client_address)
         data = connection.recv(1024)
         if data:
            print("Recieved:",data.decode('UTF-8'))
            message="Hello"
            connection.sendall(message.encode('UTF-8'))
      finally:
         connection.close()
         print("connection closed")
if __name__=='__main__':
   start_server()
