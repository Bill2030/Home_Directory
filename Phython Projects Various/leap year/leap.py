def Checkleap(year):
    if (year % 4 == 0 )or (year % 100 != 0)and (year % 400 == 0):
        print("Given year is a leap year")
    else:
        print("Given year not a leap year")

year = int(input("Enter the year"))
Checkleap(year)