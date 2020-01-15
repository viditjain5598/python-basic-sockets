import socket
import time 

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1234))
HEADERSIZE = 10

while True:
    full_msg = ""
    time.sleep(2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234)) 
    new_msg = True
    while True:
        msg = s.recv(12)
        if len(msg) <= 0:
            break

        if not new_msg:
            full_msg += msg.decode("utf-8")
        
        if new_msg:
            new_msg = False
            msg_len = int(msg[:HEADERSIZE])
            full_msg += msg.decode("utf-8")[HEADERSIZE:]

        if len(full_msg) >= msg_len:
            print(full_msg)
            break


