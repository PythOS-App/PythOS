import sysdeps as sysd
import ftxtdeps as ftd
import kbdhndlr as kbdh
import os

def enterToContinue(coloured=True):
    input(f"{ftd.Style.DIM if coloured else ""}Press {kbdh.SysKey.CONTINUE} to continue...{ftd.Style.RESET}")

def getFileDir(file=None):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    if not file == None:
        return os.path.join(scriptDir, file)
    else:
        return scriptDir
