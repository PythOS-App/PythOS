# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 13:08:33 2021

@author: Charlie K.'Captain Awesome Junior"
"""

# Changes in PythOS Indev 1.2.1: Added the possibillity to do powers in calc.

# Here is the name data in rows 12 & 13.
print("PythOS - The new way to use Python.")
print("Running PythOS on AMD64")
print()
fname = input("Type in your first name: ")
sname= input("Type in your surname: ")
print()
print()
def load():
    
   print("Loading PythOS. Please wait...")
   if fname == "admin" and sname == "admin":
       print("Welcome to PythOS. You currently have admin permisions.")
   if fname == "Test" and sname == "123":
       print("Welcome to PythOS. Dev Mode activated.")
   else:
       print("Welcome to PythOS, ", fname, sname,".")
   print("WARNING: DO NOT CLOSE THIS WINDOW UNTIL PYTHOS SAYS IT IS SAFE TO.")
load()
# Now PythOS has loaded, we can create the actual operating system.
print("You can type in commands to use PythOS. You can use commands like:")
print("power - Brings up power options")
print("ver - Brings up info about your version of PythOS")
print("settings - Lets you manage settings")
print("calc - Opeens Calculator")
UtillityOption = input("Type in your option: ")
if UtillityOption == "power":
    print("Here are your power options:")
    print("shutdown - Saves your work and lets you close the window.")
    PowerOption = input("Type in your option... ")
    if PowerOption == "shutdown":
        print("PythOS Indev v1.2.0")
        print("You can now close this window.")
    else:
        rerun = input("Error 1: The power option you have typed is not a proper power option. Press ENTER")

if UtillityOption == "ver":
    print("PythOS Indev v1.2.0")
    print("CONFIDETIONAL PROPERTY! If leaked, please email me at captainawesomejnr@outlook.com.au .")
    print("(C) Captainawesomejnr 2022. All rights reserved.")
 
if UtillityOption == "settings":
    print("SETTINGS")
    print("Here you can manage settings. Here are the settings you can manage:")
    print("1. Processor type")
    setting = input("Which setting would you like to modify?")
    if setting == "1":
        print("Select processor type:")
        print("1. 64-bit")
        print("2. 32-bit")
        processor = input("Put in your option: ")
        if processor == "1":
            print("Running PythOS on AMD64")
        if processor == "2":
            print("Running PythOS on x86")
        else:
            rerun = input("Error 3: Processor type selection didn't work. Maybe you made a typo? Press ENTER.")
    else:
         rerun = input("Error 2: Setting not found. Press ENTER")
if UtillityOption == "calc":
    CalcFirstNumber = float(input("Type in your first number: "))
    CalcOperation = input("What operation would you like to use? (* = Times, / = Divided By, ^ = Power) ")
    CalcSecondNumber = float(input("Type in the other number: "))
    if CalcOperation == "+":
        print(CalcFirstNumber, "+", CalcSecondNumber, "=", CalcFirstNumber + CalcSecondNumber)
    if CalcOperation == "-":
        print(CalcFirstNumber, "-", CalcSecondNumber, "=", CalcFirstNumber - CalcSecondNumber)
    if CalcOperation == "*":
        print(CalcFirstNumber, "*", CalcSecondNumber, "=", CalcFirstNumber * CalcSecondNumber)
    if CalcOperation == "/":
        print(CalcFirstNumber, "/", CalcSecondNumber, "=", CalcFirstNumber / CalcSecondNumber)
    if CalcOperation == "^":
        print(CalcFirstNumber,"^",CalcSecondNumber, "=", CalcFirstNumber ** CalcSecondNumber)
    
    else:
        print("Error 4: Your calculation could not be processed.")