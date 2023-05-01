from socket import socket


def send_msg(skt: socket, msg: str) -> bool:
    """
    sends a message over a socket
    """
    print(f"sending [{msg}]")
    b_msg = bytes(msg + "\n", "utf-8")  # Append a newline character
    bytesSent = 0

    while bytesSent < len(b_msg):
        print("sending some bytes...")
        bytesSent += skt.send(b_msg)
        print(f"sent {bytesSent}/{len(b_msg)}")

    return True


def recv_msg(skt: socket) -> str:
    """
    receives a message over a socket
    """
    print(f"waiting for msg")
    msg = ""
    tempBuff = bytes("", "utf-8")

    while True:
        tempBuff = skt.recv(1)
        if not tempBuff:
            break
        char = tempBuff.decode("utf-8")
        if char == "\n":  # Break the loop if a newline character is received
            break
        msg += char

    print(f"received [{msg}]")
    return msg
