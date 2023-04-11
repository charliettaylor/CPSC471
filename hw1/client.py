from socket import socket, AF_INET, SOCK_STREAM

serverName = "localhost"
serverPort = 8000


def upload(fileName: str) -> bool:
  try:
      file = open(fileName, "r")
  except:
    print("File not found")
    return False

  data = file.read()
  file.close()

  data = "upload " + fileName + " " + str(len(data))
  data = bytes(data, "utf-8")

  print(data)

  bytesSent = 0
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))

  while bytesSent < len(data):
    bytesSent += clientSocket.send(data)

  # TODO: upload file here

  clientSocket.close()

  return True


def download(fileName: str) -> str:
  data = "download " + fileName
  data = bytes(data, "utf-8")

  print(data)

  bytesSent = 0
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))

  while bytesSent < len(data):
    bytesSent += clientSocket.send(data)

  # TODO: Receive file from server

  clientSocket.close()

  file = "dummy string"
  return file


print("Welcome to the file transfer client, do you want to upload or download?")
while True:
  print("Enter 'upload' or 'download' to continue, or 'exit' to quit")
  command = input()
  if command == "upload":
    print("Please enter the name of the file you wish to upload")
    fileName = input()
    success = upload(fileName)

    if success:
      print("File uploaded successfully")
    else:
      print("File upload failed")

  elif command == "download":
    print("Please enter the name of the file you wish to download")
    fileName = input()

    file = download(fileName)

    if file != "ERROR":
      print("File downloaded successfully")
    else:
      print("File download failed")

  elif command == "exit":
    break
  else:
    print("Invalid command")