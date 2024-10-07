from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, gipot, osnov: int):
        self.gipot = gipot
        self.osnov = osnov

    def area(self):
        return self.gipot * self.osnov * 1/2


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 8)

    circle_area = circle.area()
    rectangle_area = rectangle.area()
    triangle_area = triangle.area()

    print("Площадь круга:", circle_area)
    print("Площадь прямоугольника:", rectangle_area)
    print("Площадь треугольника:", triangle_area)
    try:
        shape = Shape()
    except TypeError as e:
        print(f"Ошибка: {e}")

