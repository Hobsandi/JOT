import os, logging
from modules import  alert

def windowsShell(inp):
    commands = inp.split(" ")
    arg = commands[-1]
    if len(commands) > 1:
        func = commands[0]
        if func == "cd":
            os.chdir(arg)
        elif func == "mkdir":
            os.mkdir(arg)
        elif func == "rmdir":
            os.rmdir(arg)
        elif func == "alert":
            alert.alert(arg)
        else:
            stream = os.popen(inp)
            return(stream.read())
    else:
        # if inp == command:
        #    ...
        stream = os.popen(inp)
        return(stream.read())
    return(None)
