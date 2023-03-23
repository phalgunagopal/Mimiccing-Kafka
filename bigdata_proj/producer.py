import socket
import json

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Producer connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        list=[]
        print("Enter Topic Name...")
        msg1 = input("> ")
        if msg1 == DISCONNECT_MSG:
            list.append(msg1)
            msg=json.dumps(list)
            client.send(msg.encode(FORMAT))
            break
        print("Enter the message now...")
        msg2 =input("> ")
        list.append(msg1)
        
        list.append(msg2)
        list.append("pro")
        msg = json.dumps(list) 
        try :

            client.send(msg.encode(FORMAT))

            if msg2 == DISCONNECT_MSG:
                connected = False
            else:
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")
        except:
            print("hello world")
            client.close()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((IP,5567))
            client.send(msg.encode(FORMAT))
            if msg2 == DISCONNECT_MSG:
                connected = False
            else:
                msg = client.recv(SIZE).decode(FORMAT)
                msg=json.loads()
                print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()