'''
Задание "Они все так похожи":

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

'''


import math

class Figure:

    def __init__(self, sides, color, filled=False):
        self.__sides = sides
        self.__color = list(color)
        self.filled = filled
        self.sides_count = len(sides)


    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        return all(0 <= i <= 255 for i in (r, g, b))
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides == list(new_sides)

class Circle(Figure):
    def __init__(self, color, radius, filled=False):
        sides = [1]
        super().__init__(sides, color, filled)
        self.radius = radius
    def get_square(self):
        return math.pi * (self.__radius **2)
    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if self.get_sides():
            self.__radius = self.get_sides()[0] / (2 * math.pi)

class Triangle(Figure):
    def __init__(self, color, a, b, c, filled=False):
        sides = [a,b,c,]
        super().__init__(color, sides, filled)
    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - c))

class Cube(Figure):
    def __init__(self, color, side_lenght, filled = False):
        sides = [side_lenght] * 12
        super().__init__(color, sides, filled)
    def get_volume(self):
        sid_coun = self.get_sides()
        return sid_coun[0] ** 3 if sid_coun else 0


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
