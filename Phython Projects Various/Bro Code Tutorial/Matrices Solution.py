
rows = int(input("How many rows ? "))
columns = int(input("How many columns"))
symbol = input("Enter the symbol to use")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()