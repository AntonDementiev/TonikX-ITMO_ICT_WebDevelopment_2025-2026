import socket

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Сервер запущен на {HOST}:{PORT}")

data, addr = server_socket.recvfrom(1024)
print(data.decode())

server_socket.sendto("Hello, client".encode(), addr)
