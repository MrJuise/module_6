'''
Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и прочие свойства,
т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.

Пункты задачи:

    Создайте классы Vehicle и Sedan.
    Напишите соответствующие свойства в обоих классах.
    Не забудьте сделать Sedan наследником класса Vehicle.
    Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.
'''



class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'white', 'BLACK'] # доступные цвета
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner) # владелец
        self.__model = str(__model) # модель
        self.__engine_power = int(__engine_power) # мощность
        self.__color = str(__color) # цвет
    def get_model(self):
        print(f'Модель: {self.__model}')
    def  get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        print(f'Цвет авто: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        col = [el.upper() for el in self.__COLOR_VARIANTS]
        if new_color.upper() in col:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BlAcK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
