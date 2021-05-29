class Circle():

    # class object attributes
    pi = 3.14

    def __init__(self, radius = 1) -> None:
        self.radius = radius
        self.area = self.pi * self.radius * radius

    def circumference(self):
        return 2 * self.pi * self.radius

c = Circle(10)
print(c.radius)
print(c.area)
print(c.circumference())