'''
Задание "Они все так похожи":

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

'''


class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = list(map(int, sides))
        self.filled = bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if i == int and i > 0:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides) * self.sides_count

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            return [self.__sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        import math
        self.__radius = self.__sides / (2 * math.pi)

    def get_square(self):
        import math
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides
        import math
        grad = 60
        self.__height = self.__sides * math.sin(math.radians(grad))

    def get_square(self):
        return self.__sides[0] * self.__height / 2

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides]

    def get_volume(self):
        return self.__sides[0] ** 3



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
