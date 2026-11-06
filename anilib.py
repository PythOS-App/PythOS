import time

class Text:
    def typewriter(text, duration, trailing = "\n"):
        for char in text:
          print(char, end = "")
        print("", end = trailing)

class App:
    class Load:
        def fakeLoad(duration, name=None):
            if name == None:
                print("Loading...", end=" ")
            else:
                print(f"Loading {name}...", end=" ")
            for percent in range(0,100):
                print(f"{str(percent)}%")
                time.sleep(duration)
                todel = len(f"{str(percent)}%")
                for i in range(0,todel):
                    print("\x1b[P", end="")
        