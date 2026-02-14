import socket
import threading
import os

PORT = int(os.environ.get("PORT", 5555))
HOST = "0.0.0.0"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server running on {HOST}:{PORT}")

clients = []

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            for c in clients:
                if c != conn:
                    c.send(data)

    except:
        pass

    print(f"Client disconnected: {addr}")
    clients.remove(conn)
    conn.close()

def start():
    print("Waiting for connections...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
