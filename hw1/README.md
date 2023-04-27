# Programming Assignment 1

Objective: Create a simple FTP type server to allow upload and download of files.

## Protocol
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