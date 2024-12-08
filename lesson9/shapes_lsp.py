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

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

def display_area(shape: Shape):
    print(f"Shape's area: {shape.calculate_area()}")

if __name__ == "__main__":
    circle = Circle(radius = 9)
    rectangle = Rectangle(width = 4, height = 7)
    square = Square(side = 8)

    display_area(circle)
    display_area(rectangle)
    display_area(square)
