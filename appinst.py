import ftxtdeps as ftd
import appdeps as appd
import sysdeps as sysd
import importlib
import templates

sysmodules = ["syslang", "appdeps", "ftxtdeps", "sysdeps"]

sysVerPath = templates.getFileDir("sysver.txt")

with open(sysVerPath, "r", encoding="utf-8") as file:
    sysver = file.read()

def appInfo():
    return "PythOS App Installer"

def appInstall(appName):
    # Check if the app is already installed
    if appName in appd.openList():
        print(f"{ftd.Fore.YELLOW}Warning: {appName} is already installed. Updating...{ftd.Style.RESET}")
    input(f"Press Enter to run and install {appName}...")
    try:
        app = importlib.import_module(appName)
        try:
            appDescription = app.appInfo()
        except AttributeError:
            appDescription = input(f"{ftd.Fore.YELLOW}Warning: The app '{appName}' does not conform to the PythOS app standard. Please provide a description for this app: ")
        # Create a new entry for the app in the list
        appd.addApp(appName, appDescription)
        appd.saveList()
        input(f"{ftd.Fore.GREEN}{appDescription} ({appName}) has been successfully installed!{ftd.Style.RESET}")
        ftd.Screen.CLEAR()
    except ImportError:
        input(f"{ftd.Fore.RED}Error: App '{appName}' not found.{ftd.Style.RESET}")
        ftd.Screen.CLEAR()
    
def appLoop():
    running = True
    while running:
        ftd.Screen.CLEAR()
        print(f"{ftd.Style.BOLD}PythOS App Installer {ftd.Style.NORMAL + ftd.Style.DIM}Version: {sysver}{ftd.Style.NORMAL}")
        appName = input("Enter the name of the app you want to install (or type 'exit' to quit): ").strip().lower()
        
        if appName == "exit":
            print("Exiting the installer.")
            running = False
            break
        elif appName == "main":
            sysd.stopCode("sys_not_app", "PythOS App Installer", "Cannot install core system functions as apps.")
            ftd.Screen.CLEAR()
        elif appName in sysmodules:
            sysd.stopCode("dep_not_app", "PythOS App Installer", "Cannot install system dependencies as apps.")
            ftd.Screen.CLEAR()
        elif appName:
            ftd.Screen.CLEAR()
            appInstall(appName)
        else:
            sysd.stopCode("no_app_name", "PythOS App Installer", "No app name was provided. Please enter a valid app name.")
            ftd.Screen.CLEAR()

if __name__ == "__main__":
    appLoop()
