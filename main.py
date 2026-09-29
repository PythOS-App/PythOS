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
            
            print(f"{ftd.Fore.GREEN}PythOS has been shut down.{ftd.Style.RESET}")
        else:
            try:
                app = importlib.import_module(appSelection)
            except Exception:
                sysd.stopCode("63-72-75-6E", "app_launch_error", f"The app '{appSelection}' could not be launched.")
    else:
        sysd.stopCode("63-72-75-6E", "cmd_unknown", "That command is not recognized. Please select a valid app from the list.")
    
    
