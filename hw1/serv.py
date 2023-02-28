from socket import *
import sys

if len(sys.argv) != 3:
  print(sys.argv)
  print("Please supply address and port for server to run on")
  exit(1)

addr = sys.argv[1]
port = sys.argv[2]

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(addr, port)
serverSocket.listen(1)

print("Server is ready to receive")

data = ""

while True:
  connectionSocket, addr = serverSocket.accept()
  tempBuff = ""

  while len(data) != 40:
    tempBuff = connectionSocket.recv(40)
    if not tempBuff:
      break
    data += tempBuff

  data = connectionSocket.recv(4096)
  print(data)

  connectionSocket.close()