from os import name
import socket
from tkinter import Message
import time

def dain():
    temp=1
    print("ss")
    host = '192.168.0.130'
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    test()
    try:
        s.connect((host,port))
    except:
        print("hello")
    name = "pc2"
    while True:
        loss=str(205)
        message=name+'_'+str(temp)+'_'+loss
        print(message)
        try:
            s.send(message.encode('ascii'))
        except:
            time.sleep(0.1)
            continue
        try:
            data = s.recv(1024)
            print('Received fr bvcbthe server :',str(data.decode('ascii')))
            temp+=1
        except:
            print('hello')
        
        if True:
            time.sleep(0.1)
            continue
        
        else:
            break
    s.close()


def test():
    print("hello")

print(0)
dain()
