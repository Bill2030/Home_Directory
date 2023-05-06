Height = float(input("Enter your Height in Centimeters :"))
Weight = float(input("Enter your weight in Kg :"))
Height = Height/100
BMI = Weight/(Height * Height)
print("Your Body Mass index is: ", BMI)
if (BMI>0):
    if(BMI<=16):
        print("You are severely Underweight")
    elif(BMI <=18.5):
        print("You are Underweight")
    elif(BMI<=25):
        print("You are healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are severely overweight")





