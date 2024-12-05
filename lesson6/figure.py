class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"S = {self.width * self.height}")

rectangle1 = Rectangle(30, 20)
rectangle2 = Rectangle(40, 24)

rectangle1.calculate_area()
rectangle2.calculate_area()
