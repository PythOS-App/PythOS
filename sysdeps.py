import platform
import signal
import sys
import time
import os
from ftxtdeps import *
import kbdhndlr as key


if platform.system() == "Darwin":
    continueKey = "Return"
else:
    continueKey = "Enter"

if platform.system() == "Darwin":
    keyboardInterruptCombo = "⌘C"
else:
    keyboardInterruptCombo = "Ctrl-C"

class SysKey:
    END = keyboardInterruptCombo
    GO  = continueKey


def clear():
    # 'nt' means Windows, 'posix' covers Linux and macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def gracefulShutdown(sig, frame):
    clear()
    if key.keyboardInterruptBehaviour == key.ExitBehaviours.NORMQUIT:
        sys.exit("PythOS has been quit.")
    else:
        stopCode("unknownInterruptBehaviour", "kbdhndlr", "The interrupt behaviour specidied id unknown to the system. Perhaps you need to update?")

def stopCode(errorcode, origin, description):
    clear()
    key.keyboardInterruptBehaviour = key.ExitBehaviours.NORMQUIT
    input(f"""{Fore.RED}ERROR!{Style.RESET}
PythOS ran into a critical error and can't recover.

     Origin: {origin}
 Error Code: {errorcode}
Description: {description}

Press ENTER to quit the program.
{Style.DIM}Note: You can press {keyboardInterruptCombo} to quit PythOS, although your work will NOT be saved.""")

# Register the SIGINT signal (Ctrl+C) handler
signal.signal(signal.SIGINT, gracefulShutdown)
