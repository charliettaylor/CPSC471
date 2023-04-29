from socket import socket, AF_INET, SOCK_STREAM
import sys

from common import *

def send_listing():
    pass

def send_file():
    pass

def receive_file(skt: socket, filename: str, size: int):
    data = recv_msg(skt, size)
    if len(data) == size:
        send_msg(skt, "OK")
        with open(filename, "w") as f:
            f.write(data)
            print(f"saved {filename}")
    else:
        send_msg(skt, "ER")

if len(sys.argv) != 3:
    print(sys.argv)
    print("Please supply address and port for server to run on")
    exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((hostname, port))
serverSocket.listen(1)

data = bytes("", "utf-8")

while True:
    print(f"Server waiting for connection on {hostname}:{port}...")
    connectionSocket, addr = serverSocket.accept()
    print(f"got connection from {addr}")
    tempBuff = bytes("", "utf-8")

    # RECEIVE COMMAND
    data = recv_msg(connectionSocket)

    # INTERPRET COMMAND
    match data:
        case "UP":
            print("client wants to send a file")
            send_msg(connectionSocket, "OK")
            metadata = recv_msg(connectionSocket, 99)
            print(metadata)
            tokens = metadata.split()
            name = tokens[0]
            size = int(tokens[1])
            send_msg(connectionSocket, "OK")
            receive_file(connectionSocket, name, size)

    connectionSocket.close()
