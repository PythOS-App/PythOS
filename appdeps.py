import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.join('C:\Users\s1089491\OneDrive - Haileybury\PythOS')
filePath = os.path.join(BASE_DIR, 'applist.json')
#filePath = r'C:\Users\s1089491\OneDrive - Haileybury\PythOS\applist.json'
data = {}
appList = {}

def openList():
    with open(filePath, 'r', encoding='utf-8') as file:
        # Load the JSON data into a Python variable
        appList = json.load(file)
        return appList

def saveList():
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


