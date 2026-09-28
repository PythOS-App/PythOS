from sysdeps import *
from ftxtdeps import *
import os
import platform
import tkinter as tk
from tkinter import filedialog
import zipfile

def SetupStopCode(errorcode, origin, description):
    clear()
    input(f"""{Fore.RED}ERROR!{Style.RESET}
PythOS ran into a critical error and can't recover.

     Origin: {origin}
 Error Code: {errorcode}
Description: {description}

Press ENTER to quit Setup.""")

with open("sysver.txt", "r", encoding="utf-8") as file:
    sysver = file.read()

def banner(stage):
    if stage == 0:
        print(f"""Pyth{Fore.BLUE}O{Fore.YELLOW}S{Style.RESET} Setup
""")
    else:
        print(f"""Pyth{Fore.BLUE}O{Fore.YELLOW}S{Style.RESET} Setup - Stage {stage}
""")

banner(0)
print(f"""Welcome to PythOS {sysver} Setup!
This guided setup will help you install PythOS on your machine.""")
input(f"Press {SysKey.GO} to start setup...")

validFolder = False
while validFolder == False:
    clear()

    banner(1)
    print("First of all we need a location to install PythOS in.")
    input(f"Press {SysKey.GO} to select a folder to install PythOS in...")

    # Initialize tkinter and hide the main background window
    root = tk.Tk()
    root.withdraw()

    # Open the folder picker dialog and capture the selected path
    #folder_path = filedialog.askdirectory(title="Select Install Folder")
    folder_path = r"C:\Users\s1089491\PythOS"
    # Print or use the returned folder path
    if folder_path:
        print(f"Selected folder: {folder_path}")
        try:
            input(f"Press {SysKey.GO} to install, or press {SysKey.END} to exit setup...")
            validFolder = True
        except KeyboardInterrupt:
            pass
    else:
        print(f"{Fore.RED}User cancelled the folder selection.")
        input(f"Press {SysKey.GO} to try again...")


# 1. Automatically find the script's current folder
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Set the exact ZIP name and your destination variable
zip_filename = "source.zip"
source_zip_path = os.path.join(script_dir, zip_filename)

# 3. Ensure the target folder exists
os.makedirs(folder_path, exist_ok=True)

# 4. Extract the ZIP while preserving the internal directory layout
try:
    with zipfile.ZipFile(source_zip_path, 'r') as zip_ref:
        zip_ref.extractall(folder_path)
    print(f"Successfully installed PythOS in: {folder_path}")
    input(f"Press {SysKey.GO} to continue setup...")
    
except FileNotFoundError:
    SetupStopCode("ZipNotFound","setup",f"'source.zip' was not found in the script directory ({script_dir}).")
except zipfile.BadZipFile:
    SetupStopCode("BadZip","setup","'source.zip' is corrupted or not a valid ZIP file.")




