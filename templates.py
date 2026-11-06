import sysdeps as sysd
import ftxtdeps as ftd
import kbdhndlr as kbdh

def enterToContinue(coloured=True):
    input(f"{ftd.Style.DIM if coloured else ""}Press {kbdh.SysKey.CONTINUE} to continue...{ftd.Style.RESET}")
