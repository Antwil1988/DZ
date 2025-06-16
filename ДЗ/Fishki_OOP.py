""" Singleton """


class Logger:
    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        self._logs.append(message)

    def get_logs(self):
        return self._logs


# Реализация
logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

# Проверка на Singleton
assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]

print("Логгер работает как Singleton!")

""" SOLID (S) """


class Report:

    def __init__(self, title, content):
        self.title = title
        self.content = content


class PDFGenerator:

    @staticmethod
    def generate(report):
        print(f"Generating PDF: {report.title}")
        return f"{report.title}.pdf"


class ReportSaver:

    @staticmethod
    def save_to_file(content, filename):
        print(f"Saving report to file: {filename}")
        return True


# Реализация

report = Report("Report", "This is the content")

pdf_generator = PDFGenerator()
pdf_filename = pdf_generator.generate(report)

saver = ReportSaver()
saver.save_to_file(report.content, pdf_filename)

print("Completed!")

""" SOLID (O) """

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


# PayPal
class PayPalProcessor(PaymentProcessor):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"[PayPal] Оплата {amount} руб. с аккаунта {self.email}")


# Кредитная карта
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"[CreditCard] Оплата {amount} руб. с карты {self.card_number}")


# Криптовалюта
class CryptoProcessor(PaymentProcessor):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"[Crypto] Оплата {amount} руб. с кошелька {self.wallet_address}")


# Реализация
paypal = PayPalProcessor("user@example.com")
card = CreditCardProcessor("1234-5678-9012-3456")
crypto = CryptoProcessor("0xABCDEF123456")

for processor in [paypal, card, crypto]:
    processor.pay(1000.0)

""" SOLID (L) """

from abc import ABC, abstractmethod


# Абстрактный класс для всех птиц
class Bird(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def speak(self):
        pass


# Отдельный класс для летающих птиц
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(FlyingBird):
    def walk(self):
        print("воробей идёт")

    def speak(self):
        print("Чирик-чирик!")

    def fly(self):
        print("воробей летит!")


class Penguin(Bird):
    def walk(self):
        print("Пингвин идёт")

    def speak(self):
        print("Крях-крях!")


def bird_activity(bird: Bird):
    bird.walk()
    bird.speak()


def flying_activity(bird: FlyingBird):
    bird.fly()


birds = [Sparrow(), Penguin()]
for bird in birds:
    bird_activity(bird)

flying_activity(Sparrow())
# flying_activity(Penguin())  # Ошибка


""" SOLID (I) """

from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def run(self): pass

class Flyable(ABC):
    @abstractmethod
    def fly(self): pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass


# Лев реализует только то, что нужно
class Lion(Runnable):
    def run(self):
        print("Лев бежит.")

lion = Lion()
lion.run()

""" staticmethod, classmethod, property """


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(celsius: float):
        return celsius <= 0

# Реализация
t1 = Temperature(25)
print(f"Цельсий: {t1.celsius}°C, Кельвин: {t1.kelvin}K")
print("Замерзание:", Temperature.is_freezing(t1.celsius))

# Реализация
t2 = Temperature.from_fahrenheit(32)
print(f"Цельсий: {t2.celsius}°C, Кельвин: {t2.kelvin}K")
print("Замерзание:", Temperature.is_freezing(t2.celsius))