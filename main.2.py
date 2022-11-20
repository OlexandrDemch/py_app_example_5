import math

a = int(input("1 - area, 2 - perimeter:"))


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Enter radius of circle: "))
obj = circle(r)
if a == 1:
    print("Area of circle:", round(obj.area(), 2))
elif a == 2:
    print("Perimeter of circle:", round(obj.perimeter(), 2))