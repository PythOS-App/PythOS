import ftxtdeps as ftd
from ftxtdeps import Style, Fore, Back, Screen, AutoReset
import json
import sysdeps as sysd

def appInfo():
    return "PythOS Settings"

def importSettings():
    with open('settings.json', 'r', encoding='utf-8') as file:
        # This returns a LIST of dictionaries
        appList = json.load(file)
        return appList

def writeSettings():
    with open('settings.json', 'w', encoding='utf-8') as file:
        appList = json.dump(settingsList, file, indent=4)

with open("sysver.txt", "r", encoding="utf-8") as file:
    sysver = file.read()

# Load your settings list
settingsList = importSettings()

running = True
while running:
    sysd.clear()
    print(f"{ftd.Style.BOLD}PythOS Settings {ftd.Style.NORMAL + ftd.Style.DIM}Version: {sysver}{ftd.Style.NORMAL}")
    print("You can change the following settings:")
    
    # 1. Loop through the list and display the friendly names with a number
    for index, setting in enumerate(settingsList, start=1):
        print(f"{index}. {setting['friendlyName']}")
    print(f"{len(settingsList) + 1}. Exit")

    # 2. Get the user's choice
    choice = input("\nSelect a setting by number to change it: ").strip()

    # 3. Process the user's choice
    try:
        choice_num = int(choice)
        
        # Check if the user chose to exit
        if choice_num == len(settingsList) + 1:
            print("Exiting settings menu.")
            writeSettings()
            running = False
            break
        
        # Check if the number corresponds to a valid setting
        elif 1 <= choice_num <= len(settingsList):
            # Target the specific setting dictionary (adjusting for 0-based index)
            selected_setting = settingsList[choice_num - 1]
            
            print(f"\nYou selected: {selected_setting['friendlyName']}")
            print(f"Current Value: {selected_setting['state']}")
            
            # --- DO SOMETHING HERE ---
            # For example, ask them for a new value:
            new_value = input("Enter new value: ")
            
            # (Optional) Handle type conversion for booleans if needed
            if isinstance(selected_setting['state'], bool):
                selected_setting['state'] = new_value.lower() in ['true', '1', 'yes']
            else:
                selected_setting['state'] = new_value
                
            input(f"""{ftd.Fore.GREEN}{ftd.Style.BOLD}Updated successfully!{ftd.Style.RESET}\nPress Enter to continue...""")
            
        else:
            print(f"{ftd.Fore.RED + ftd.Style.BOLD}Invalid choice. Please pick a number from the list.{ftd.Style.RESET}")
        
    except ValueError:
        print("Please enter a valid number.")
