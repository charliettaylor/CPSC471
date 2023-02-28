from socket import *

serverName = "ecs.fullerton.edu"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverName, serverPort)

data = "Hello world! This is how long my pen15 is"
bytesSent = 0

while bytesSent != len(data):
  bytesSent += clientSocket.send(data)

clientSocket.close()