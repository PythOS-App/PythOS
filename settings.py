import ftxtdeps as ftd
from ftxtdeps import Style, Fore, Back, Screen, AutoReset
import json
import sysdeps as sysd
import re
import syslang

def appInfo():
    return "PythOS Settings"

def importSettings():
    with open('settings.json', 'r', encoding='utf-8') as file:
        appList = json.load(file)
        return appList

def writeSettings():
    with open('settings.json', 'w', encoding='utf-8') as file:
        json.dump(settingsList, file, indent=4) # Fixed assignment bug here

def appLoop():
    with open("sysver.txt", "r", encoding="utf-8") as file:
        sysver = file.read()

    settingsList = importSettings()

    running = True
    while running:
        # If sysd.clear matches ftd.Screen.CLEAR(), make sure it has () too!
        sysd.clear() 
        print(f"{ftd.Style.BOLD}PythOS Settings {ftd.Style.NORMAL + ftd.Style.DIM}Version: {sysver}{ftd.Style.NORMAL}")
        print("You can change the following settings:")
        
        for index, setting in enumerate(settingsList, start=1):
            print(f"{index}. {setting['friendlyName']}")
        print(f"{len(settingsList) + 1}. Exit")

        choice = input("\nSelect a setting by number to change it: ").strip()

        try:
            choice_num = int(choice)
            
            if choice_num == len(settingsList) + 1:
                print("Exiting settings menu.")
                writeSettings()
                running = False
                break
            
            elif 1 <= choice_num <= len(settingsList):
                selected_setting = settingsList[choice_num - 1]
                
                print(f"\nYou selected: {selected_setting['friendlyName']}")
                print(f"Current Value: {selected_setting['state']}")
                
                if selected_setting['identifier'] == "sys.language":
                    # This directly modifies selected_setting in memory automatically!
                    syslang.setLang(selected_setting)
                else:
                    new_value = input("Enter new value: ")
                    if selected_setting['datatype'] == "bool":
                        selected_setting['state'] = new_value.lower() in ['true', '1', 'yes']
                    else:
                        selected_setting['state'] = new_value
                
                # Save right away so memory and disk always match up
                writeSettings()
                input(f"""\n{ftd.Fore.GREEN}{ftd.Style.BOLD}Updated successfully!{ftd.Style.RESET}\nPress Enter to continue...""")
                
            else:
                print(f"{ftd.Fore.RED + ftd.Style.BOLD}Invalid choice. Please pick a number from the list.{ftd.Style.RESET}")
            
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    appLoop()