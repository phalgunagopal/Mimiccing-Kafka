import socket
import sys
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
    print(f"[CONNECTED] Consumer connected to server at {IP}:{PORT}")
    counter=0
    connected = True
    while connected:
        list=[]
        msg = input("> ")
        list.append(msg)
        if len(sys.argv)==2:
            list.append("conflag")
        else:
            list.append("con")
        
       

        if msg[0] == DISCONNECT_MSG:
            connected = False
        else:
            msg = json.dumps(list)
            client.send(msg.encode(FORMAT))
            msg1 = client.recv(SIZE).decode(FORMAT)
            msg2=json.loads(msg1)
            print(f"[SERVER] {msg2}")
            
            ack=client.recv(SIZE).decode(FORMAT)
            ack=json.loads(ack)
            counter=counter+1
            print(ack)
            

if __name__ == "__main__":
    main()