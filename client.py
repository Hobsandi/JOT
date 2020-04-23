import socket

addr = ("192.168.10.119",1337)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
currentworking = s.recv(1024).decode("utf-8")
while 1:
    inp = input(currentworking + ">")
    if inp.isspace() or not inp:
        continue
    s.sendall(inp.encode("utf-8"))
    response = s.recv(1024).decode("utf-8")
    if "cd" in inp:
        currentworking = response
    elif response != None:
        print(response)
    elif response == None or isspace(response):
        print("Response was none")
        print(response)
        continue
