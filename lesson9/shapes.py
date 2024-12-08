from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class AreaCalculator:
    @staticmethod
    def calculate(shape: Shape):
        return shape.calculate_area()

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    circle = Circle(radius = 7)
    rectangle = Rectangle(width = 3, height = 4)
    triangle = Triangle(base = 5, height = 8)

    print(f"Circle's area: {AreaCalculator.calculate(circle)}")
    print(f"Rectangle's area: {AreaCalculator.calculate(rectangle)}")
    print(f"Triangle's area: {AreaCalculator.calculate(triangle)}")
