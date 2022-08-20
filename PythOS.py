# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 13:08:33 2021

@author: Charlie K.'Captain Awesome Junior"
"""

# Changes in PythOS Indev 2.0.1: Added special 'crash' utility that looks like corruption (The utillity is called '$CORRUPT$' (without the quotation marks) and when there are dollar signs ($) it means it is a easter egg.)

# Here is the name data in rows 15 & 16.
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
ShutDown = False
load()
# Now PythOS has loaded, we can create the actual operating system. But, we need to make a loop so that you can type in a command and then type in a new one.
while ShutDown == False:
    print()
    print("You can type in commands to use PythOS. You can use commands like:")
    print("power - Brings up power options")
    print("ver - Brings up info about your version of PythOS")
    print("settings - Lets you manage settings")
    print("calc - Opens Calculator")
    UtillityOption = input("Type in your option: ")
    if UtillityOption == "power":
        print("Here are your power options:")
        print("shutdown - Saves your work and lets you close the window.")
        PowerOption = input("Type in your option... ")
        if PowerOption == "shutdown":
            print("PythOS Indev v2.0.0")
            print("You can now close this window.")
            ShutDown = True
            break
        else:
                rerun = input("Error 1: The power option you have typed is not a proper power option. Press ENTER")
    elif UtillityOption == "ver":
                    print("PythOS Indev v2.0.0")
                    print("CONFIDETIONAL PROPERTY! If leaked, please email me at captainawesomejnr@outlook.com.au .")
                    print("(C) Captainawesomejnr 2022. All rights reserved.")
                    
    elif UtillityOption == "settings":
                        print("SETTINGS")
                        print("Here you can manage settings. Here are the settings you can manage:")
                        print("1. Processor type")
                        setting = input("Which setting would you like to modify? ")
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
    elif UtillityOption == "calc":
                                    CalcFirstNumber = float(input("Type in your first number: "))
                                    CalcOperation = input("What operation would you like to use? (* = Times, / = Divided By, ^ = Power) ")
                                    CalcSecondNumber = float(input("Type in the other number: "))
                                    if CalcOperation == "/" and CalcSecondNumber == 0:
                                        print(CalcFirstNumber, "/ 0.0: Error processing (Could not divide by 0.)")
                                    else:
                                        if CalcOperation == "+":
                                            print(CalcFirstNumber, "+", CalcSecondNumber, "=", CalcFirstNumber + CalcSecondNumber)
                                        elif CalcOperation == "-":
                                            print(CalcFirstNumber, "-", CalcSecondNumber, "=", CalcFirstNumber - CalcSecondNumber)
                                        elif CalcOperation == "*":
                                                print(CalcFirstNumber, "*", CalcSecondNumber, "=", CalcFirstNumber * CalcSecondNumber)
                                        elif CalcOperation == "/":
                                                print(CalcFirstNumber, "/", CalcSecondNumber, "=", CalcFirstNumber / CalcSecondNumber)
                                        elif CalcOperation == "^":
                                                print(CalcFirstNumber,"^",CalcSecondNumber, "=", CalcFirstNumber ** CalcSecondNumber)
                                        else:
                                                rerun = input("Error 4: Your calculation could not be processed. Press ENTER.")
    # Below is some fun to make it look like PythOS has been corrupted!
    elif UtillityOption == "$CORRUPT$":
        from random import randint
        CORRUPT_Lines = 0
        while CORRUPT_Lines <= 20:
            CORRUPT_Letters = randint(1, 3)
            if CORRUPT_Letters == 1:
                print("@@@@@@@@@@@@@@@@@@@@@@@@")
            elif CORRUPT_Letters == 2:
                print("########################")
            else:
                print("$$$$$$$$$$$$$$$$$$$$$$$$")
            CORRUPT_Lines = CORRUPT_Lines + 1
    else:
                rerun = input("Error 0: The utillity you have typed is not a proper utillity option. Press ENTER")