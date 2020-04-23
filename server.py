import socket, os, shell


addr = (socket.gethostbyname("0.0.0.0"),1337)
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
    if "cd" in command:
        sendCwd(conn)
    elif output != None or output == '' or not output:
        conn.sendall(output.encode("utf-8"))
        print("Sent output.")
    else:
        conn.sendall(b"-")
        print("Output was none.")
        continue
