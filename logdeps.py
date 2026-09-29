import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(BASE_DIR, 'pythoslog.json')

data = {}
log = {}

def openLog():
    with open(filePath, 'r', encoding='utf-8') as file:
        # Load the JSON data into a Python variable
        appList = json.load(file)
        return appList

def saveLog():
    with open(filePath, "w") as file:
        json.dump(data, file, indent=4)
    openLog()

def addEntry(cmd, description):
    log[cmd] = description
    saveLog()

openLog()