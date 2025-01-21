import socket
def start_client():
   client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   server_address =('127.0.0.1',53)
   try:
      client_socket.connect(server_address)
      print("connected to server in port 53")
      message ="Hello"
      client_socket.sendall(message.encode('utf-8'))
      print("sent:",message)
      data = client_socket.recv(1024)
      print("Recieved:",data.decode("utf-8"))
   finally:
      client_socket.close()
      print("connection closed")
if __name__=='__main__':
   start_client()
