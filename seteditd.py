import json
import os
from typing import Any, List, Optional


class ConfigManager:

    def __init__(self, filepath: str):
        # Initialises the manager and loads the JSON file.
        self.filepath = filepath
        self.data: List[dict] = []
        self.load()

    def load(self) -> None:
        # Loads data from the JSON file or initialises an empty list if the file doesn't exist.
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = []
        else:
            self.data = []

    def save(self) -> None:
        # Saves the current state back to the JSON file. 
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def _find_entry(self, identifier: str) -> Optional[dict]:
        # Helper method to find an entry by its unique identifier.
        for entry in self.data:
            if entry.get("identifier") == identifier:
                return entry
        return None

    def add_entry(
        self,
        identifier: str,
        friendly_name: str,
        state: Any,
        datatype: str,
        modifiable: bool = True,
    ) -> bool:
        """Adds a new entry if the identifier does not already exist."""
        if self._find_entry(identifier):
            print(f"Error: Identifier '{identifier}' already exists.")
            return False

        new_entry = {
            "identifier": identifier,
            "friendlyName": friendly_name,
            "state": state,
            "datatype": datatype,
            "modifiable": modifiable,
        }
        self.data.append(new_entry)
        self.save()
        return True

    def remove_entry(self, identifier: str) -> bool:
        # Removes an entry by its identifier.
        entry = self._find_entry(identifier)
        if entry:
            self.data.remove(entry)
            self.save()
            return True
        print(f"Error: Identifier '{identifier}' not found.")
        return False

    def update_state(self, identifier: str, new_state: Any) -> bool:
        # Updates only the 'state' value of a specific identifier.
        entry = self._find_entry(identifier)
        if entry:
            entry["state"] = new_state
            self.save()
            return True
        print(f"Error: Identifier '{identifier}' not found.")
        return False

    def get_entry(self, identifier: str) -> Optional[dict]:
        # Retrieves a specific entry by its identifier.
        return self._find_entry(identifier)
