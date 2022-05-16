class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def surface_area(self, number):
        print("{} cm2, and the number is {}.".format(Circle.pi*self.radius**2, number))

    def circumference(self, number):
        print("{} cm, and the number is {}.".format(Circle.pi*2*self.radius, number))

my_circle = Circle(1)

my_circle.circumference(6)
my_circle.surface_area(4)