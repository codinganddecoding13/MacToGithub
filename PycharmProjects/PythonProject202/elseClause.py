# try/except/else

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)

input("\n\nPress the enter key to exit. ")