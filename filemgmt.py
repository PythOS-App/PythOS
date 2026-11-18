import json
import os
from typing import Any, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.join('C:\Users\s1089491\OneDrive - Haileybury\PythOS')

class App:
    def readList():
        with open(filePath, 'r', encoding='utf-8') as file:
            # Load the JSON data into a Python variable
            appList = json.load(file)
        if appList == {} or appList == None:
            saveList({"exit": "Exit PythOS", "settings": "PythOS Settings", "appinst": "PythOS App Installer"})
            return {"exit": "Exit PythOS", "settings": "PythOS Settings", "appinst": "PythOS App Installer"}
        else:
            return appList

    def saveList(data=appList):
        with open(filePath, "w") as file:
            json.dump(data, file, indent=4)

    def addApp(cmd, description):
        appList[cmd] = description
        
    def delApp(cmd):
        try:
            del appList[cmd]
        except:
            pass

    def modifyApp(cmd, description):
        delApp(cmd)
        addApp(cmd, description)

    def __init__(self):
        filePath = os.path.join(BASE_DIR, 'applist.json')
        #filePath = r'C:\Users\s1089491\OneDrive - Haileybury\PythOS\applist.json'
        data = {}
        appList = {}
        readList()

class Settings:

    def __init__(self, filepath: str = os.fath.join(BASE_DIR, "settings.json")):
        # Initialises the manager and loads the JSON file.
        self.filepath = filepath
        self.data: List[dict] = []
        self.load()

    def load(self) -> None:
        """Loads data from the JSON file or initialises an empty list."""
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = []
        else:
            self.data = []

    def save(self) -> None:
        """Saves the current state back to the JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def _find_entry(self, identifier: str) -> Optional[dict]:
        """Helper method to find an entry by its unique identifier."""
        for entry in self.data:
            if entry.get("identifier") == identifier:
                return entry
        return None

    def _infer_datatype(self, value: Any) -> str:
        """Intelligently detects the datatype string based on the Python value."""
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, (list, tuple)):
            return "list"
        if isinstance(value, dict):
            return "dict"
        return "str"  # Defaults to string for text or anything else

    def add_entry(
        self,
        identifier: str,
        friendly_name: str,
        state: Any,
        modifiable: bool = True,
    ) -> bool:
        """Adds a new entry and infers the datatype automatically."""
        if self._find_entry(identifier):
            print(f"Error: Identifier '{identifier}' already exists.")
            return False

        new_entry = {
            "identifier": identifier,
            "friendlyName": friendly_name,
            "state": state,
            "datatype": self._infer_datatype(state),
            "modifiable": modifiable,
        }
        self.data.append(new_entry)
        self.save()
        return True

    def update_state(self, identifier: str, new_state: Any) -> bool:
        """Updates the state and re-evaluates the datatype dynamically."""
        entry = self._find_entry(identifier)
        if entry:
            entry["state"] = new_state
            entry["datatype"] = self._infer_datatype(new_state)
            self.save()
            return True
        print(f"Error: Identifier '{identifier}' not found.")
        return False

    def remove_entry(self, identifier: str) -> bool:
        """Removes an entry by its identifier."""
        entry = self._find_entry(identifier)
        if entry:
            self.data.remove(entry)
            self.save()
            return True
        print(f"Error: Identifier '{identifier}' not found.")
        return False

    def get_entry(self, identifier: str) -> Optional[dict]:
        """Retrieves a specific entry by its identifier."""
        return self._find_entry(identifier)



