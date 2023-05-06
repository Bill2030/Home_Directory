# *args = Parameter that will pack all the arguments into a tuple
# Its useful so that the function can accept a varying amount of arguments.

def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(2,3))
# in the above it will work because we have provided only two arguments

#lets add the third argument below and see if it works!
def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(2,3,4))

#print(add(2,3, 7))
# it gives the error that only two positional arguments but three given and to solve this we use
#*args

def add(*args):
    sum = 0
    for i in args: # We loop through to have many arguments
        sum += i
    return sum

print(add(1,2,3,6,7,8))







