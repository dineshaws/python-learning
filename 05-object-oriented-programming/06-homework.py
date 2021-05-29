class Line():
    def __init__(self, c1, c2) -> None:
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        return (y2-y1)/(x2-x1)

c1 = (3, 2)
c2 = (8, 10)
line = Line(c1, c2)
print(line.distance())
print(line.slope())


class Cylinder():
    def __init__(self, height=1, radius =1) -> None:
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height*3.14*(self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())