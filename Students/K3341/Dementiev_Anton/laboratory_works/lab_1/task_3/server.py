import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Сервер запущен: http://{HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Подключен клиент: {addr}")
            request = conn.recv(1024).decode()
            print("Запрос:\n", request)

            try:
                with open("index.html", "r", encoding="utf-8") as f:
                    body = f.read()
            except FileNotFoundError:
                body = "<h1>404 Not Found</h1>"

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                f"Content-Length: {len(body.encode('utf-8'))}\r\n"
                "\r\n"
                f"{body}"
            )

            conn.sendall(response.encode("utf-8"))
