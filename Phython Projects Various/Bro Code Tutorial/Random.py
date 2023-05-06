import random

x = random.randint(1,6) # use for specific numbers

print(x)

y = random.random()  # Useful when the numbers are not specified
print(y)

my_list = ["rock", "paper", "scissors"]
z = random.choice(my_list) # Useful when using the list
print(z)

cards =[ 1,2,3,4,5,6,7,8,9,"K","Q","A"]
random.shuffle(cards) # Useful for shuffling the cards
print(cards)