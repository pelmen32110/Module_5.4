'''
В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
'''
class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, numbers_of_floors):  # количество этажей в доме
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self,new_floor): #переход на этаж
        if self.numbers_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
            return None
        for i in range(new_floor+1):
            print(i)

    def __len__(self): #проверка высоты дома
        return self.numbers_of_floors

    def __str__(self): #вывод информации о доме
        return f'Название: {self.name}, количество этажей {self.numbers_of_floors}'

    def __eq__(self, other): # сравнение ==
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        return NotImplemented

    def __lt__(self, other): # сравнение <
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        return NotImplemented

    def __le__(self, other): # сравнение <=
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        return NotImplemented

    def __gt__(self, other): # сравнение >
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        return NotImplemented

    def __ge__(self, other): # сравнение =>
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        return NotImplemented

    def __ne__(self, other): # сравнение !=
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        return NotImplemented

    def __add__(self, value): # добавление новых этажей
        if isinstance(value, int):
            self.numbers_of_floors = self.numbers_of_floors + value
        return self


    def __radd__(self, value): # так же, как __add__()
        return self.__add__(value)

    def __iadd__(self, value): # так же, как __add__()
        return self.__add__(value)

    def __del__(self):
        print(self.name," снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)