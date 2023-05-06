import random

min_val = 1
max_val = 6

# To loop the rolling through the user input
roll_again = "yes"
# Loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dices....")
    print("The values are :")
    # Generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
    # Generating and printing second random integer from 1 to 6
    print(random.randint(min_val, max_val))
# asking the user to roll the dice again. Any input other than Yes or Y will be terminated

roll_again = input("Roll the Dices again")
