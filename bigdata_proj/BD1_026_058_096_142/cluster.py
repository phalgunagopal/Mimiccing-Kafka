import socket
import threading
import json
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = [5566,5567,5568]
ADDR = (IP, PORT[0])
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
brokers=['Brokers/b1','Brokers/b2','Brokers/b3']
leader=brokers[0]
brokers.remove(leader)
k=leader

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    counter=0
    connected = True
    dict={}
    while connected:
        msg = conn.recv(SIZE).decode()
        msg = json.loads(msg)
       
        if msg[0] == DISCONNECT_MSG:
            connected = False
            continue
        
        print(f"[{addr}] {msg}")
        msgs = f"Msg received: {msg}"
        print(f"Consumer requests {msg}")
        print(msg[1])

        # consumer
        if len(msg)==2:
            try:
                
                path1="/".join([leader, msg[0]])
                print(os.path.exists("/".join([path1,f"{msg[0]}_01"])))
                with open("/".join([path1,f"{msg[0]}_01"])) as fp:
                    messages1=fp.readlines()
                    lines1 = len(messages1)
                    

                with open("/".join([path1,f"{msg[0]}_02"])) as fp:
                    messages2=fp.readlines()
                    lines2 = len(messages2)
                    
                
                with open("/".join([path1,f"{msg[0]}_03"])) as fp:
                    messages3=fp.readlines()
                    lines3 = len(messages3)
                    
                messages=messages1+messages2+messages3
                messages=json.dumps(messages)
            
                
                total=lines1+lines2+lines3
                
                if msg[1]=="conflag":
                    
                    conn.send(messages.encode(FORMAT))
                    counter=counter+1
                    
                    
                # elif msg[1]=="con":
                #     readalready=total//3
                #     conn.send(messages[total-1:].encode(FORMAT))
                #     print(total)
            except:
                print("[CONSUMER] Disconnected")
            


            #this is sent by consumer
            
        
        # producer
        else:
            Exist = os.path.exists("/".join([leader, msg[0]]))

            if Exist:
                try:
                    k=dict[msg[0]]%3
                except:
                    dict[msg[0]]=1
                
                path1="/".join([leader, msg[0]])
                path2="/".join([brokers[0], msg[0]])
                path3="/".join([brokers[1], msg[0]])
                
                if dict[msg[0]]%3 == 0:
                    with open("/".join([path1,f"{msg[0]}_01"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path2,f"{msg[0]}_01"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path3,f"{msg[0]}_01"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    dict[msg[0]]=dict[msg[0]]+1
                    print("file exists")
                elif dict[msg[0]]%3 == 1:
                    with open("/".join([path1,f"{msg[0]}_02"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path2,f"{msg[0]}_02"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path3,f"{msg[0]}_02"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    dict[msg[0]]=dict[msg[0]]+1
                    print("file exists")
                else:
                    with open("/".join([path1,f"{msg[0]}_03"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path2,f"{msg[0]}_03"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    with open("/".join([path3,f"{msg[0]}_03"]), 'a') as f:
                        print(msg[1])
                        f.write(msg[1])
                        f.write('\n')
                    dict[msg[0]]=dict[msg[0]]+1
                    print("file doesnt exist")
                print("file exists")

            else:
                dict[msg[0]]=1
                print(dict)
                path1="/".join([leader, msg[0]])
                path2="/".join([brokers[0], msg[0]])
                path3="/".join([brokers[1], msg[0]])
                os.makedirs(path1)
                os.makedirs(path2)
                os.makedirs(path3)

                f01 = open("/".join([path1,f"{msg[0]}_01"]),"w")
                f02= open("/".join([path1,f"{msg[0]}_02"]),"w")
                f03 = open("/".join([path1,f"{msg[0]}_03"]),"w")

                f01.close()
                f02.close()
                f03.close()
                    
                f11 = open("/".join([path2,f"{msg[0]}_01"]),"w")
                f12= open("/".join([path2,f"{msg[0]}_02"]),"w")
                f13 = open("/".join([path2,f"{msg[0]}_03"]),"w")

                f11.close()
                f12.close()
                f13.close()

                f21 = open("/".join([path3,f"{msg[0]}_01"]),"w")
                f22= open("/".join([path3,f"{msg[0]}_02"]),"w")
                f23 = open("/".join([path3,f"{msg[0]}_03"]),"w")

                f21.close()
                f22.close()
                f23.close()

                with open("/".join([path1,f"{msg[0]}_01"]), 'a') as f:
                    print(msg[1])
                    f.write(msg[1])
                    f.write('\n')
                with open("/".join([path2,f"{msg[0]}_01"]), 'a') as f:
                    print(msg[1])
                    f.write(msg[1])
                    f.write('\n')
                with open("/".join([path3,f"{msg[0]}_01"]), 'a') as f:
                    print(msg[1])
                    f.write(msg[1])
                    f.write('\n')
                print("file doesnt exist")

            #this is sent by producer 
        msgs=json.dumps(msgs)
        conn.send(msgs.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f" [ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()