
print("Welcome to the treasure highland you mission is to find the treasure")
choice1 = input("Which path do you want to go 'left' or 'right' ?\n").lower()
if choice1 == left:
    choice2 =input("Do you want to swim or 'wait' or 'boat'? \n").lower()
    if choice2 == boat:
        choice3=input("You are almost finding the treasure which door to open 'Red','Blue', or 'Yellow'\n").lower()
        if choice3 == Red:
            print("Game over you have been engulfed by fire")
        elif choice3 == Blue:
            print("Game over you are in the ocean")
        elif choice3 == Yellow:
            print("Congratulations you found the trasure you win")
        else:
            print("You loose")
    else:
        print("Game over you have been attacked by crocodile")

else:
    print("you have chosen the wrong path game over")






