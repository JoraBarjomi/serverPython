import socket

client = socket.socket()
# hostname = "147.45.48.64"
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))
while True:
    msg = input("Enter message to server: ")
    if msg == "quit": 
        break
    client.send((msg + "\n").encode())
    data = client.recv(1024)
    print("Server sent: ", data.decode())
client.close()