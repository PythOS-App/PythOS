def appLoop():
    CalcFirstNumber = float(input("Type in your first number: "))
    CalcOperation = input("What operation would you like to use?\n\n* = Multiplication\n/ = Division\n^ = Exponentiation")
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
                rerun = input("Error: Your calculation could not be processed. Press ENTER to continue.")
def appInfo():
    return "Calculator"
