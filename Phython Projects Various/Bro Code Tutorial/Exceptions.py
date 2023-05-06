# Exceptions are events detected during execution that interrupts the flow of a program

try:
    numerator = int(input("Enter the number to divide: "))
    denominator = int(input("Enter the number to divide by"))
    result = numerator / denominator
    print(round(result))
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Only numbers be used")
except Exception:
    print("something went wrong")
else:
    print(round(result))
    pause: 3:10

