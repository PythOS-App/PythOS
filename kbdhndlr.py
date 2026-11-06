import platform

class ExitBehaviours:
    NORMQUIT   = "normalQuit"
    SQUIT      = "suppressedQuit"
    DEVCONSOLE = "console"

keyboardInterruptBehaviour = ExitBehaviours.NORMQUIT

if platform.system() == "Darwin":
    continueKey = "Return"
else:
    continueKey = "Enter"

if platform.system() == "Darwin":
    keyboardInterruptCombo = "⌘C"
else:
    keyboardInterruptCombo = "Ctrl-C"

class SysKey:
    EXIT      = keyboardInterruptCombo
    CONTINUE  = continueKey
