import sysdeps as sysd
import ftxtdeps as ftd
import json
import os
import templates
availableLanguages = ["en","zh","ru","de"]

settingsPath = templates.getFileDir("settings.json")

def importSettings():
    with open(settingsPath, "r", encoding="utf-8") as file:
        appList = json.load(file)
        return appList

with open(settingsPath, "r", encoding="utf-8") as file:
    sysver = file.read()

settingsList = importSettings()

def get_setting_by_id(identifier, filename=settingsPath):
    for item in settingsList:
        if item["identifier"] == identifier:
            return item
    return None

langEntry = get_setting_by_id("sys.language")

def currentlang():
    return langEntry["state"] if langEntry else setLang(langEntry)

# Added target_setting parameter here
def setLang(target_setting):
    if target_setting is None:
        return ""
        
    success = False
    while not success:
        # FIX: Added parentheses () to execute the screen clear command
        ftd.Screen.CLEAR() 
        
        print(f"{ftd.Style.BOLD}Set a new language:{ftd.Style.RESET}")
        print(f"{ftd.Style.BOLD if target_setting['state'] == 'en' else ''}1. English{ftd.Style.RESET}")
        print(f"{ftd.Style.BOLD if target_setting['state'] == 'zh' else ''}2. 汉语{ftd.Style.RESET}")
        print(f"{ftd.Style.BOLD if target_setting['state'] == 'ru' else ''}3. Русский{ftd.Style.RESET}")
        print(f"{ftd.Style.BOLD if target_setting['state'] == 'de' else ''}4. Deutsch{ftd.Style.RESET}")
        new_value = input("Your selection: ").strip().lower()

        if new_value.startswith("1") or "en" in new_value:
            target_setting["state"] = "en"
            success = True
        elif new_value.startswith("2") or "zh" in new_value or "ch" in new_value:
            target_setting["state"] = "zh"
            success = True
        elif new_value.startswith("3") or "ru" in new_value:
            target_setting["state"] = "ru"
            success = True
        elif new_value.startswith("4") or "de" in new_value or "ge" in new_value:
            target_setting["state"] = "de"
            success = True
        else:
            sysd.stopCode("langUnknown", "sys", f"The language entered is not supported in PythOS {sysver}. Try upgrading your PythOS version.")
    
    return target_setting["state"]

def langCheck():
    if langEntry is None:
        setLang(langEntry)
    elif langEntry["state"] == "":
        setLang(langEntry)
    elif langEntry["state"] in availableLanguages:
        pass
    else:
        setLang(langEntry)
