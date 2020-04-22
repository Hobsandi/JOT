import socket, os, shell

addr = ("127.0.0.1",1337)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen()

def sendCwd(connection):
    print("Sending cwd.")
    conn.sendall(os.getcwd().encode("utf-8"))
conn, addr = server.accept()
print("Connected")
sendCwd(conn)
while 1:
    command = conn.recv(1024).decode("utf-8")
    print("Command recieved:",command)
    output = shell.windowsShell(command)
    if output != None:
        conn.sendall(output.encode("utf-8"))
        print("Sent output.")
    else:
        if "cd" in command:
            sendCwd(conn)
        print("Output was none.")
        continue
