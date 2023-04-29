from socket import socket, AF_INET, SOCK_STREAM
import sys

from common import send_msg, recv_msg


def send_command(skt: socket, msg: str) -> bool:
    """
    sends a command over a socket and waits for confirmation
    """
    send_msg(skt, msg)
    confirm = recv_msg(skt)

    if confirm != "OK":
        print("Server didn't acknowledge command properly")
        skt.close()
        return False

    return True


def send_metadata(skt: socket, meta: str):
    """
    sends metadata over a socket and waits for confirmation
    """
    send_msg(skt, meta)
    confirm = recv_msg(skt)

    if confirm != "OK":
        print("Server could not receive metadata")
        skt.close()
        return False

    return True


def send_file(skt: socket, file: str) -> bool:
    """
    sends a file over a socket and waits for confirmation
    """
    send_msg(skt, file)
    confirm = recv_msg(skt)

    if confirm != "OK":
        print("Server could not receive file")
        skt.close()
        return False

    return True


def upload(fileName: str) -> bool:
    try:
        file = open(fileName, "r")
    except:
        print("File not found")
        return False

    data = file.read()
    file.close()

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((addr, port))

    if not send_command(clientSocket, "UP"):
        return False

    meta = fileName.strip() + " " + str(len(data)) + " "
    if not send_metadata(clientSocket, meta):
        return False

    if not send_file(clientSocket, data):
        return False

    clientSocket.close()
    return True


def download(fileName: str) -> bool:
    data = "download " + fileName
    data = bytes(data, "utf-8")

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((addr, port))

    if not send_command(clientSocket, "DL"):
        return False

    # send filename to server
    if not send_msg(clientSocket, fileName):
        return False

    # receive size of file
    size = int(recv_msg(clientSocket, 10))

    if size == 0:
        print("File not found")
        clientSocket.close()
        return False

    # confirm client ready to download
    if not send_msg(clientSocket, "OK"):
        return False

    # receive file
    data = recv_msg(clientSocket, size)
    clientSocket.close()

    # write file to disk
    with open(fileName, "w") as f:
        f.write(data)

    return True


if len(sys.argv) != 3:
    print(sys.argv)
    print("Please supply address and port of server to connect to")
    exit(1)

addr = sys.argv[1]
port = int(sys.argv[2])

print("Welcome to the file transfer client, do you want to upload or download?")
while True:
    print("Enter 'upload' or 'download' to continue, or 'exit' to quit")
    command = input()
    if command == "upload":
        print("Please enter the path/name of the file you wish to upload")
        fileName = input()
        success = upload(fileName)

        if success:
            print("File uploaded successfully")
        else:
            print("File upload failed")

    elif command == "download":
        print("Please enter the name of the file you wish to download")
        fileName = input()

        success = download(fileName)

        if success:
            print("File downloaded successfully")
        else:
            print("File download failed")

    elif command == "exit":
        break
    else:
        print("Invalid command")
