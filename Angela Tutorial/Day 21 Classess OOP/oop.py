# This show the inheritance from the main family
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale", "exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__() # This is called inheritance

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breath()
