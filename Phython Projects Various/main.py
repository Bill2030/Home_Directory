import random

number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("Enter guess "))
    if (guess < number):
        print("Guess Higher ")
    elif (guess > number):
        print("guess lower ")
    else:
        print("You won ")

