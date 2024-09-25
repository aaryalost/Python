from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimeter(self):
        pass 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width + self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 3

    def perimeter(self):
        return 2 * 3.14 * self.radis

rect = Rectangle(10, 20)
circle = Circle(5)

print(f"Rectangle Area: {rect.area()}")  

print(f"Rectangle Perimeter: {rect.perimeter()}") 

print(f"Circle Area: {circle.area()}")       

print(f"Circle Perimeter: {circle.perimeter()}")  
