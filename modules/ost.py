import os

def main():
    stream = os.popen("dir C:\\Users")
    users = []
    for i in stream.readlines():
        if "<DIR>" in i:
            c = i.split(" ")
            if "." not in c[-1]: 
                users.append(c[-1])
    print("Pick a user: ")
    for i in users:
        print(users.index(i)+1, i)
    choice = input("")
    user = users[int(choice)-1].strip()
    print("Changing directory into", user +"s Desktop")
    os.chdir("C:\\Users\\" + user + "\\Desktop\\")
    
