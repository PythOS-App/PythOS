import sysdeps as sysd
import appdeps as appd
import ftxtdeps as ftd
import importlib

appList = appd.openList()
appCmds = []

cmdLineRunning = True
while cmdLineRunning:
    sysd.clear()
    print("What app do you want to launch?")
    for index, (key, value) in enumerate(appList.items(), start = 1):
        print(f"{key}: {value}")
        appCmds.append(key)
        
    appSelection = input("> ")
    if appSelection in appCmds:
        if appSelection == "exit":
            cmdLineRunning = False
            print("PythOS has been shut down.")
        else:
            try:
                app = importlib.import_module(appSelection)
            except:
                sysd.stopCode("63-72-75-6E", "app_launch_error")
    else:
        sysd.stopCode("63-72-75-6E", "cmd_unknown")
    
    
