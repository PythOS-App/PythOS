# The *fancy* text dependency

import sys

class Fore:
    BLACK   = "\x1b[30m"
    RED     = "\x1b[31m"
    GREEN   = "\x1b[32m"
    YELLOW  = "\x1b[33m"
    BLUE    = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN    = "\x1b[36m"
    WHITE   = "\x1b[37m"

class Back:
    BLACK   = "\x1b[40m"
    RED     = "\x1b[41m"
    GREEN   = "\x1b[42m"
    YELLOW  = "\x1b[43m"
    BLUE    = "\x1b[44m"
    MAGENTA = "\x1b[45m"
    CYAN    = "\x1b[46m"
    WHITE   = "\x1b[47m"

class Style:
    BOLD       = "\x1b[1m"
    DIM        = "\x1b[2m"     # The dim/faint code
    NORMAL     = "\x1b[22m"    # Turns off ONLY Bold and Dim (leaves colors alone)
    RESET      = "\x1b[0m"     # Turns off EVERYTHING (colors + fonts)

def autoResetPause():
    """Stop auto-resetting lines automatically."""
    if isinstance(sys.stdout, FancyStreamWrapper):
        sys.stdout.enabled = False

def autoResetResume():
    """Re-engage line-by-line auto-resetting and clear remaining styles."""
    if isinstance(sys.stdout, FancyStreamWrapper):
        sys.stdout.enabled = True
    # Bypass print and push the reset sequence directly to the underlying terminal
    _ORIGINAL_STDOUT.write("\x1b[0m")
    _ORIGINAL_STDOUT.flush()


class FancyStreamWrapper:
    # A proxy stream that intercepts standard prints to inject resets. 
    def __init__(self, wrapped_stream):
        self.wrapped_stream = wrapped_stream
        self.enabled = True  # Added enabled flag for pause/resume functions

    def write(self, text):
        # Restored bulletproof newline auto-reset logic.
        # This keeps your multi-colored banners safe from mid-line resets!
        if self.enabled and text == "\n":
            self.wrapped_stream.write("\x1b[0m\n")
        else:
            self.wrapped_stream.write(text)

    def flush(self):
        """Required so functions like print() can clear the buffer."""
        self.wrapped_stream.flush()

# =======================================================
# INITIALISATION FOR WINDOWS (conhost.exe zero-dependency)
# =======================================================

# 1. Keep a permanent backup of the original terminal output stream
_ORIGINAL_STDOUT = sys.stdout

# 2. Force Windows to enable native Virtual Terminal (ANSI) support
if sys.platform == "win32":
    try:
        import ctypes
        from ctypes import wintypes

        # Set up constants for Windows Kernel console handles
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        
        # CRITICAL FIX: Configure ctypes to handle 64-bit Windows pointers correctly
        kernel32.GetStdHandle.argtypes = [wintypes.DWORD]
        kernel32.GetStdHandle.restype = ctypes.c_void_p
        
        STD_OUTPUT_HANDLE = -11  # Equivalent to DWORD 4294967285 cast unsigned
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004

        # Get handle to current standard output console
        hOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        
        # Check against typical 64-bit invalid handle values
        if hOut and hOut != ctypes.c_void_p(-1).value: 
            dwMode = wintypes.DWORD()
            # Fetch current console mode
            if kernel32.GetConsoleMode(ctypes.c_void_p(hOut), ctypes.byref(dwMode)):
                # Combine current flags with Virtual Terminal flag
                newMode = dwMode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
                # Apply new mode directly to conhost.exe
                kernel32.SetConsoleMode(ctypes.c_void_p(hOut), newMode)
                
                # Send an anchor flush to register the console mode
                _ORIGINAL_STDOUT.write("\x1b[0m")
                _ORIGINAL_STDOUT.flush()
    except Exception:
        pass  # Fail gracefully if it runs in a headless environment

# 3. Hijack stdout with your custom proxy stream
sys.stdout = FancyStreamWrapper(_ORIGINAL_STDOUT)
