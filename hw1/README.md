# File Transfer by Python (FTP) - Programming Assignment 1

Objective: Create a simple FTP type server to allow upload and download of files.

Group Members
- Charlie Taylor - ctaylor27@csu.fullerton.edu
- Alex Tran - altran@csu.fullerton.edu
- Mark Carbajal - markc9090@csu.fullerton.edu
- Abraham Medina - abrahammda@csu.fullerton.edu

We used Python for this assignment, and you will need to run the client and server separately. 

```
// To run the server, use the format below
python3 serv.py <hostname> <port>

// To run the client, use the format below
python3 client.py <hostname> <port>
```

## Protocol
Here is a quick description of how our protocol works for the client and server communicating. Each line indicates the data being sent

### Upload
- client: "UP"
- server: "OK" | "ER"
- client: FILENAME FILESIZE
- server: "OK" | "ER"
- client: FILE
- server: "OK" | "ER"

### Download
- client: "DL"
- server: "OK" | "ER"
- client: FILENAME
- server: FILESIZE
- client: "OK" | "ER"
- server: FILE

### List

- client: "LS"
- server: "OK" | "ER"
- server: FILES_AVAILABLE