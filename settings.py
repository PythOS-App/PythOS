import ftxtdeps as ftd
import ftxtdeps as ftd
import json
import sysdeps as sysd
import re # regular expressions
import syslang
import os

def appInfo():
    return "PythOS Settings"

def importSettings():
    with open('settings.json', 'r', encoding='utf-8') as file:
        appList = json.load(file)
        return appList

# 1. Added 'data' as an argument here
def writeSettings(data):
    file_path = 'settings.json'
    temp_file = file_path + ".tmp"
    
    try:
        # 1. Write data to a temporary file first
        with open(temp_file, 'w') as file:
            json.dump(data, file, indent=4)
            
        # 2. Safely replace the old file with the new one
        # This operation is atomic—if the system crashes, your old file is untouched!
        os.replace(temp_file, file_path)
        
    except Exception as e:
        print(f"Error saving settings: {type(e).__name__}: {e}")
        # Clean up the temp file if it was created
        if os.path.exists(temp_file):
            os.remove(temp_file)

def appLoop():
    with open("sysver.txt", "r", encoding="utf-8") as file:
        sysver = file.read()

    settingsList = importSettings()

    running = True
    while running:
        
        ftd.Screen.CLEAR()
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
                # 2. Passed settingsList here
                writeSettings(settingsList)
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
                
                # 3. Passed settingsList here too
                writeSettings(settingsList)
                input(f"""\n{ftd.Fore.GREEN}{ftd.Style.BOLD}Updated successfully!{ftd.Style.RESET}\nPress Enter to continue...""")
                
            else:
                print(f"{ftd.Fore.RED + ftd.Style.BOLD}Invalid choice. Please pick a number from the list.{ftd.Style.RESET}")
            
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    appLoop()
