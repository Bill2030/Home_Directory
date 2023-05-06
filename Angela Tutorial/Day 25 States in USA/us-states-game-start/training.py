class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return (self.x + self.y)

v1 = Vector(10, 20)
v2 = Vector(50, 60)
print(v1.add())
print(v2.add())
