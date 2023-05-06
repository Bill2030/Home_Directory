# Key Word Arguments are the arguments preceded by the identifier when we pass them to a function
#The order of the arguments doesnt matter unlike positional arguments
#python knows the names of our arguments that our function receives.

def hello(first_name, middle_name,last_name):
   print("Hello" + first_name + middle_name + last_name)

(hello(middle_name="Bro", last_name="Code",first_name="dude"))

# As above once you assign the key arguments it doesnt matter the position unlike the positional arguments
# They are preceded by identifier
#  in this case are middle_name = , first_name=

