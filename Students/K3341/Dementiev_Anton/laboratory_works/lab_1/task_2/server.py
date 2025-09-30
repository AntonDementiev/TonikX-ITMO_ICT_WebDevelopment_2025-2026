import socket
import math

HOST = "127.0.0.1"
PORT = 12345


def solve_quadratic(a: float, b: float, c: float) -> str:
    D = b**2 - 4 * a * c
    if D < 0:
        return "Нет действительных корней"
    elif D == 0:
        x = -b / (2 * a)
        return f"Один корень: {x}"
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Два корня: {x1}, {x2}"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Сервер слушает на {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Подключен клиент: {addr}")
        data = conn.recv(1024).decode()
        print("Получено:", data)

        parts = data.split()
        a, b, c = float(parts[0]), float(parts[1]), float(parts[2])

        result = solve_quadratic(a, b, c)
        conn.sendall(result.encode())
