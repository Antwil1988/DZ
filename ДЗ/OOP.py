""" Задание 1. Инкапсуляция """


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        """Пополнение счёта"""
        if amount > 0:
            self.__balance += amount
            return f"Пополнено {amount}. Новый баланс: {self.__balance}."
        return "Сумма для пополнения должна быть положительной"

    def withdraw(self, amount):
        """Снятие средств со счёта"""
        if amount <= 0:
            return "Сумма для снятия должна быть положительной"
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Снято {amount}. Остаток: {self.__balance}."
        return "Недостаточно средств на счёте"

    def get_balance(self):
        """Получение текущего баланса."""
        return f"Текущий баланс: {self.__balance}."


# Реализация
account = BankAccount(100)  # Создаём счёт с начальным балансом 100
print(account.deposit(50))  # Пополняем на 50
print(account.withdraw(30))  # Снимаем 30
print(account.withdraw(200))  # fail
print(account.get_balance())  # Проверяем баланс

""" Задание 2. Наследование """


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}"


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return (f"Разработчик: {self.name}, Язык: {self.programming_language}, "
                f"Должность: {self.position}, Зарплата: {self.salary}")


class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.employees = []  # Список подчинённых

    def add_employee(self, employee):
        """Добавляет сотрудника"""
        self.employees.append(employee)
        return f"Сотрудник {employee.name} добавлен"

    def get_info(self):
        return (f"Менеджер: {self.name}, Должность: {self.position}, "
                f"Зарплата: {self.salary}, Подчинённых: {len(self.employees)}")


# Реализация
dev1 = Developer("Анна", "Старший разработчик", 150000, "Python")
dev2 = Developer("Иван", "Младший разработчик", 100000, "JavaScript")
manager = Manager("Ольга", "Руководитель отдела", 170000)

manager.add_employee(dev1)
manager.add_employee(dev2)

print(dev1.get_info())
print(dev2.get_info())
print(manager.get_info())

""" Задание 3. Полиморфизм """

import math


class Shape:
    def area(self):
        """Возвращает площадь"""
        return 0

    def perimeter(self):
        """Возвращает периметр"""
        return 0


class Rectangle(Shape):
    """Прямоугольник"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f'Прямоугольник {self.length} x {self.width}'


class Circle(Shape):
    """Окружность"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Окружность с радиусом {self.radius}"


# Реализация
rectangle1 = Rectangle(4, 5)
circle1 = Circle(3)
rectangle2 = Rectangle(2, 6)
circle2 = Circle(5)

shapes = [rectangle1, circle1, rectangle2, circle2]

for shape in shapes:
    print(f"{shape}:")
    print(f"  Площадь: {shape.area():.2f}")
    print(f"  Периметр: {shape.perimeter():.2f}")

""" Задание 4. Абстракция и интерфейс """

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        """Запуск двигателя"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Остановка двигателя"""
        pass

    @abstractmethod
    def move(self):
        """Движение транспорта"""
        pass


class Car(Transport):

    def __init__(self, model):
        self.model = model
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return f"Двигатель автомобиля {self.model} запущен"
        return "Двигатель уже работает"

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return f"Двигатель автомобиля {self.model} заглушен"
        return "Двигатель уже выключен"

    def move(self):
        if self.engine_started:
            return f"Автомобиль {self.model} едет"
        return "Сначала запустите двигатель"

    def __str__(self):
        return f"Автомобиль {self.model}"


class Boat(Transport):

    def __init__(self, name):
        self.name = name
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return f"Двигатель лодки {self.name} запущен"
        return "Двигатель уже работает"

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return f"Двигатель лодки {self.name} заглушен"
        return "Двигатель уже выключен"

    def move(self):
        if self.engine_started:
            return f"Лодка {self.name} плывёт"
        return "Сначала запустите двигатель"

    def __str__(self):
        return f"Лодка {self.name}"


# Реализация
car = Car("Toyota Camry")
boat = Boat("Волна")

# авто
print(car)
print(car.start_engine())
print(car.move())
print(car.stop_engine())
print()

# лодка
print(boat)
print(boat.start_engine())
print(boat.move())
print(boat.stop_engine())

""" Задание 5. Множественное наследование """


class Flyable:

    def fly(self):
        return "I'm flying!"


class Swimmable:

    def swim(self):
        return "I'm swimming!"


class Duck(Flyable, Swimmable):

    def make_sound(self):
        return "Quack!"


# Реализация
duck = Duck()

print(duck.fly())
print(duck.swim())
print(duck.make_sound())

""" Задание 6. Комбинированное: Зоопарк """

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Flyable:
    def fly(self):
        return "летает"


class Swimmable:
    def swim(self):
        return "плавает"


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "бегает"


class Bird(Animal, Flyable):
    def speak(self):
        return "Tweet!"

    def move(self):
        return self.fly()


class Fish(Animal, Swimmable):
    def speak(self):
        return "(молчит)"

    def move(self):
        return self.swim()


# Реализация
dog = Dog()
bird = Bird()
fish = Fish()

zoo = [dog, bird, fish]

for animal in zoo:
    print(f"{animal.__class__.__name__}:")
    print(f"  Звук: {animal.speak()}")
    print(f"  Движение: {animal.move()}")
