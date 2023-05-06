# **kwargs = Parameter that will pack all the arguments into a dictionary.
# Its useful so that a function can accept a varying amount of keyword arguments.

def hello(**kwargs):
    print("Hello" + kwargs['first'] + "" + kwargs['last'])


hello(first="Bro", middle="Dude", last="code", title="Mr")