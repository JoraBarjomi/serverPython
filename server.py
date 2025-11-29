import socket

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen()
print("Server running...")
con, _ = server.accept()
while True:
    data = con.recv(1024)
    msg = data.decode()
    if not data:
        con.close()
        break
    print(f"Client send: {msg}")
    msg = msg[::-1]
    con.send(msg.encode())