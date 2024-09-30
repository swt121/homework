import math

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersection_area(self, other):
        x_inter = max(0, min(self.x + self.width, other.x + other.width) - max(self.x, other.x))
        y_inter = max(0, min(self.y + self.height, other.y + other.height) - max(self.y, other.y))
        return x_inter * y_inter

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def intersection_area(self, other):
        d = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

        if d >= self.radius + other.radius:
            return 0

        if d <= abs(self.radius - other.radius):
            return math.pi * min(self.radius, other.radius) ** 2

        r1, r2 = self.radius, other.radius

        part1 = r1 ** 2 * math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
        part2 = r2 ** 2 * math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))
        part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))

        return part1 + part2 - part3


rect1 = Rectangle(0, 0, 4, 4)
rect2 = Rectangle(2, 2, 4, 4)
circle1 = Circle(0, 0, 5)
circle2 = Circle(4, 0, 5)

print("Площадь пересечения прямоугольников:", rect1.intersection_area(rect2))
print("Площадь пересечения кругов:", circle1.intersection_area(circle2))
