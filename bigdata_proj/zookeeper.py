import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Consumer connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("> ")
        try:
            client.send(msg.encode(FORMAT))

            if msg == DISCONNECT_MSG:
                connected = False
            else:
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")
        except:
            print("hello world")
            client.close()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((IP,5567))


if __name__ == "__main__":
    main()