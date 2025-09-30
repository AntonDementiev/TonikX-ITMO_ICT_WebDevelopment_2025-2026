import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto("Hello, server".encode(), (HOST, PORT))

data, _ = client_socket.recvfrom(1024)
print(data.decode())
