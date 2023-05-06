# The region where the function is recognized.
# We have the local variable and global variable
# Local variable is only available within the function or inside the function
#Global variable is available inside and outside the function.

name = "Bro"  # This is the global variable

def display_name():
    name = "code" # this is a local variable
    print(name)

display_name()
print(name)
