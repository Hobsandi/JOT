import socket

addr = ("127.0.0.1",1337)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
currentworking = s.recv(1024).decode("utf-8")
while 1:
    inp = input(currentworking + ">")
    s.sendall(inp.encode("utf-8"))    
    response = s.recv(1024).decode("utf-8")
    if "cd" in inp:
        currentworking = response
    if response != None:
        print(response)
    else:
        continue
