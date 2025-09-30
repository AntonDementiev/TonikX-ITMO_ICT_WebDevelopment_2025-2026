import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Введите сообщение (/quit для выхода): ")
    if msg == "/quit":
        break
    client_socket.sendto(msg.encode(), (HOST, PORT))
    data, _ = client_socket.recvfrom(1024)
    print("Ответ сервера:", data.decode())

client_socket.close()
