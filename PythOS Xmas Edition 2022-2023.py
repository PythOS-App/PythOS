# -*- coding: utf-8 -*-

"""
Created on Sun Aug 29 13:08:33 2021

@author: Charlie K.'Captain Awesome Junior'
""" 

# Changes in PythOS Indev 1.0.0: Added PythOS PRO (BETA)
# To add the wait functionality, we need to import time.sleep.
from time import sleep
PythOS_Ver = "Alpha 1.0.0 Xmas Edition"
# Here is the name data in rows 18-19.
print("PythOS - The new way to use Python.")
ProcessorType = 1
print("Running PythOS on AMD64")
fname = ""
sname = ""
TryNewDev = ""
ActivatedPyPro = False
def login():
    print()
    global fname
    global sname
    fname = input("Type in your first name: ")
    sname = input("Type in your surname: ")
    print()
    print()
def load():
    print("Loading PythOS. Please wait...")
    global TryNewDev
    if fname == "admin" and sname == "admin":
       print("Welcome to PythOS. You currently have admin permisions")
    if fname == "Test" and sname == "123":
       TryNewDev = input("Developers should try the new PythOS Developer's Edition. Would you like to exit PythOS to run it?(Y/N):")
       if TryNewDev == "Y":
           print("Just a sec... ")
       else:
           print("Welcome to PythOS. Dev Mode activated.")
    else:
       print("Welcome to PythOS, ", fname, sname,".")
    print("WARNING: DO NOT CLOSE THIS WINDOW UNTIL PYTHOS SAYS IT IS SAFE TO.")
    primt("Also, MERRY XMAS!")
    return fname
    return sname
    return TryNewDev
ShutDown = False
login()
load()
# Now PythOS has loaded, we can create the actual operating system. But, we need to make a loop so that you can type in a command and then type in a new one.

while ShutDown == False:
    if TryNewDev == "Y":
           print("PythOS is shutting down so you can try PythOS Developer's Edition. Please wait...")
           sleep(5)
           print("PythOS has shut down. To install the Developer's Edition, please refer to the section titled 'Setup' in the README.md of https://github.com/Captain-Awesome-Jnr/PythOS-Dev-Edition")
           ShutDown = True
           break
    else:
        print()
        print("You can type in commands to use PythOS. You can use commands like:")
        print("power - Brings up power options")
        print("ver - Brings up info about your version of PythOS")
        print("settings - Lets you manage settings")
        if ActivatedPyPro == True:
            print("pro - Starts the PythOS Pro Workspace")
        print("launch - Opens the App Lancher, where you can open apps")
        UtillityOption = input("Type in your option: ")
        if UtillityOption == "power":
            print("Here are your power options:")
            print("shutdown - Saves your work and lets you close the window.")
            print("#shutdown - Quickly turns off PythOS (Not reccomended).")
            print("sleep - Pauses operations in PythOS and puts it into a low-power mode.")
            PowerOption = input("Type in your option... ")
            if PowerOption == "shutdown":
                print("Logging", fname, sname, """off.
This operation may take a while. Don't close this window.""")
                sleep(15)
                print("""Preparing PythOS for safe closure...
This operation may take a while. Don't close this window.""")
                sleep(20)
                print("""You have reached a point where it is safe to exit PythOS.
You can now close this window.""")
                ShutDown = True
                break
            elif PowerOption == "#shutdown":
                print("Quick Shutdown initilisation:")
                DoQuickShutdown = (input("Quick Shutdown will imedietly let you close the window. Turn off now? (Y/N): "))
                if DoQuickShutdown == "Y" or "y":
                    print("""PythOS - Shut down sucsessful: 
You can now close this window.""")
                    break
                elif DoQuickShutdown == "N" or "n":
                   print("Aborting Quick Shutdown.")
                else:
                    rerun = input("""There was an error prossesing your request:
Quick Shutdown inisilisation. Press ENTER to return to main menu.""")
            elif PowerOption == "sleep":
                print("PythOS is currently asleep.")
                ExitSleep = input("Press any key to exit sleep: ")
                if ExitSleep == "":
                    print("Welcome back,", fname, sname,".")
                else:
                    print("Welcome back", fname, sname,".")
            else:
                    rerun = input("Error 1: The power option you have typed is not a proper power option. Press ENTER")
        elif UtillityOption == "ver":
                        print("PythOS", PythOS_Ver)
                        print("CONFIDETIONAL PROPERTY! If leaked, please email me at captainawesomejnr@outlook.com.au .")
                        print("(C) Captainawesomejnr 2022-23. All rights reserved.")
        elif UtillityOption == "pro":
            if ActivatedPyPro == False:
                        print("Hmmm... It looks like PythOS Pro cannot start.")
                        sleep(5)
                        if ProcessorType == 1:
                            STOPCRASH_Run = input("""STOP!

A fatal error has occured and PythOS could not keep running. Due to this, PythOS was shut down to prevent damage to your installation.
Fatal error cause: PythOS Pro could not start.
             Code: x64-01010101-01110011-01100101-01110010
You can:
Press ENTER to terminate the pogram. It is recomended that you do this as it is the most effective fix.
                OR
Type 'close' to exit PythOS. You should not do this because it will abandon all unsaved data.

For more information, check the article about STOP! crash screens at https://www.github.com/Captain-Awesome-Jnr





Type in your option: """)
                        if STOPCRASH_Run == "":
                            print("Terminating program...")
                            sleep(2.5)
                            print("Sucsessfully terminated program. Returning to PythOS.")
                        else:
                            break
            elif ProcessorType == 2:
                STOPCRASH_Run = input("""STOP!

A fatal error has occured and PythOS could not keep running. Due to this, PythOS was shut down to prevent damage to your installation.
Fatal error cause: User-Activated Fatal Crash
             Code: x86-01010101-01110011-01100101-01110010
You can:
Press ENTER to terminate the pogram. It is recomended that you do this as it is the most effective fix.
                OR
Type 'close' to exit PythOS. You should not do this because it will abandon all unsaved data.

For more information, check the article about STOP! crash screens at https://www.github.com/Captain-Awesome-Jnr





Type in your option: """)
                if STOPCRASH_Run == "":
                    print("Terminating program...")
                    sleep(2.5)
                    print("Sucsessfully terminated program. Returning to PythOS.")
                else:
                    break
            else:
                import PyPRO as pro
                pro.run
        elif UtillityOption == "settings":
                        print("SETTINGS")
                        print("Here you can manage settings. Here are the settings you can manage:")
                        print("1. Processor type")
                        print("2. PythOS Pro Activation")
                        setting = input("Which setting would you like to modify? ")
                        if setting == "1":
                            print("Select processor type:")
                            print("1. 64-bit")
                            print("2. 32-bit")
                            processor = input("Put in your option: ")
                            if processor == "1":
                                print("Running PythOS on AMD64 or x64")
                                ProcessorType = 1
                            if processor == "2":
                                    print("Running PythOS on x86")
                                    ProcessorType = 2
                            else:
                                rerun = input("Error 3: Processor type selection didn't work. Maybe you made a typo? Press ENTER.")
                        elif setting == "2":
                            print("Here you can manage whether or not you want PythOS Pro.")
                            print("WARNING: Do not turn on PythOS Pro unless you have followed the instructions in its README.txt. This can cause PythOS to crash to the extent you need to restart it!!!")
                            activatepypro = input("""With PythOS Pro, you can:
- Use the FIRST PythOS GUI
- Enjoy games
and MUCH, MUCH MORE!
Would you like to turn PythOS Pro on? (Y/N)""")
                            if activatepypro == "Y" or "y":
                                sleep(0.5)
                                ActivatedPyPro = True
                                print("PythOS Pro is ready to be used.")
                            elif activatepypro == "N" or "n":
                                sleep(0.5)
                                ActivatedPyPro = False
                                print("PythOS Pro has been deactivated. Thank you for trying.")
                            else:
                                sleep(1.5)
                                ActivatedPyPro = False
                                print("You did not enter Y or N. For the saftey of PythOS, Pro has been deactivated.")
                        else:
                            rerun = input("Error 2: Setting not found. Press ENTER")
        elif UtillityOption == "launch":
            print("App Lancher")
            print("Here you can lanch one of the apps in PythOS. Here are the apps avalible:")
            print("1. Calculator")
            print("2. Don't click the button (*BETA*)")
            print("3. Spy Messages")
            LaunchOption  = input("Type in the number of your option: ")
            if LaunchOption == "1":
                                    CalcFirstNumber = float(input("Type in your first number: "))
                                    CalcOperation = input("What operation would you like to use? (* = Times, / = Divided By, ^ = Power) ")
                                    CalcSecondNumber = float(input("Type in the other number: "))
                                    if CalcOperation == "/" and CalcSecondNumber == 0:
                                        print(CalcFirstNumber, "/ 0: Error processing (Could not divide by 0.)")
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
            elif LaunchOption == "2":
                 import tkinter
                 Window = tkinter.Tk()
                 Button = tkinter.Button(Window, text="Do not press this button", width=40)
                 Button.pack(padx=10, pady=10)
            elif LaunchOption == "3":
                CipherAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
                CipherToEncrypt = input("Please enter a string to encrypt. ")
                CipherToEncrypt = CipherToEncrypt.upper()
                CipherShift = int(input("Please enter a integer (whole number) from 1-25 to be your key"))
                CipherMessage = ""
                for CurrentChar in CipherToEncrypt:
                    OldPos = CipherAlphabet.find(CurrentChar)
                    NewPos = OldPos + CipherShift
                    if CurrentChar in CipherAlphabet:
                        CipherMessage = CipherMessage + CipherAlphabet[NewPos]
                    else:
                        CipherMessage = CipherMessage + CurrentChar
                print("Your encrypted message is", CipherMessage)
            else:
                print("Error 4: App could not be launched.")
        # Below is some fun to make it look like PythOS has been corrupted!
        elif UtillityOption == "$CORRUPT$":
             from random import randint
             CORRUPT_Lines = 0
             while CORRUPT_Lines <= 60:
                CORRUPT_Letters = randint(1, 3)
                if CORRUPT_Letters == 1:
                    print("@@@@@@@@@@@@@@@@@@@@@@@@")
                elif CORRUPT_Letters == 2:
                    print("########################")
                else:
                    print("$$$$$$$$$$$$$$$$$$$$$$$$")
                CORRUPT_Lines = CORRUPT_Lines + 1
            
    # Below is even more fun - crashing PythOS.
        elif UtillityOption == "$STOPCRASH$":
            if ProcessorType == 1:
                STOPCRASH_Run = input("""STOP!

A fatal error has occured and PythOS could not keep running. Due to this, PythOS was shut down to prevent damage to your installation.
Fatal error cause: User-Activated Fatal Crash
             Code: x64-01010101-01110011-01100101-01110010
You can:
Press ENTER to terminate the pogram. It is recomended that you do this as it is the most effective fix.
                OR
Type 'close' to exit PythOS. You should not do this because it will abandon all unsaved data.

For more information, check the article about STOP! crash screens at https://www.github.com/Captain-Awesome-Jnr





Type in your option: """)
                if STOPCRASH_Run == "":
                    print("Terminating program...")
                    sleep(2.5)
                    print("Sucsessfully terminated program. Returning to PythOS.")
                else:
                    break
            elif ProcessorType == 2:
                STOPCRASH_Run = input("""STOP!

A fatal error has occured and PythOS could not keep running. Due to this, PythOS was shut down to prevent damage to your installation.
Fatal error cause: User-Activated Fatal Crash
             Code: x86-01010101-01110011-01100101-01110010
You can:
Press ENTER to terminate the pogram. It is recomended that you do this as it is the most effective fix.
                OR
Type 'close' to exit PythOS. You should not do this because it will abandon all unsaved data.

For more information, check the article about STOP! crash screens at https://www.github.com/Captain-Awesome-Jnr





Type in your option: """)
                if STOPCRASH_Run == "":
                    print("Terminating program...")
                    sleep(2.5)
                    print("Sucsessfully terminated program. Returning to PythOS.")
                else:
                    break
            elif UtillityOption == "$KILL$":
                break
            else:
                rerun = input("Error 0: The utillity you have typed is not a proper utillity option. Press ENTER")
