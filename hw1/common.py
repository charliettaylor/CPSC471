from socket import socket


def send_msg(skt: socket, msg: str) -> bool:
    """
    sends a message over a socket
    """
    print(f'sending [{msg}]')
    b_msg = bytes(msg, "utf-8")
    bytesSent = 0

    while bytesSent < len(b_msg):
        print('sending some bytes...')
        bytesSent += skt.send(b_msg)
        print(f'sent {bytesSent}/{len(b_msg)}')

    return True


def recv_msg(skt: socket, length: int = 2) -> str:
    """
    receives a message over a socket
    """
    print(f'waiting for msg[{length}]')
    msg = ""
    tempBuff = bytes("", "utf-8")

    while len(msg) != length:
        tempBuff = skt.recv(length)
        if not tempBuff:
            break
        msg += tempBuff.decode("utf-8")
        if msg[-1] == " ":
            break

    print(f'received [{msg}]')
    return msg
