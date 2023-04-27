from socket import socket


def send_msg(skt: socket, msg: str) -> bool:
    """
    sends a message over a socket
    """
    b_msg = bytes(msg, "utf-8")
    bytesSent = 0

    while bytesSent < len(b_msg):
        bytesSent += skt.send(b_msg)

    return True


def recv_msg(skt: socket, length: int = 2) -> str:
    """
    receives a message over a socket
    """
    msg = ""
    tempBuff = bytes("", "utf-8")

    while len(msg) != length:
        tempBuff = skt.recv(length)
        if not tempBuff:
            break
        msg += tempBuff.decode("utf-8")

    return msg
