import csv
import statistics

class Student:
    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        self.grades = grades or []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def info(self):
        return f"Öğrenci: {self.name} ({self.student_id}), Notlar: {self.grades}, Ortalama: {self.average():.2f}"


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class Book:
    def __init__(self, title, author, pages):
        if pages < 0:
            raise ValueError("Page count cannot be negative")
        self.title = title
        self.author = author
        self.pages = pages
        self.read_pages = 0

    def read(self, pages):
        if self.read_pages + pages <= self.pages:
            self.read_pages += pages
        else:
            raise ValueError("Exceeds total page count")

    def skip(self, pages):
        if 0 <= pages <= self.pages:
            self.read_pages = pages
        else:
            raise ValueError("Invalid page number")

    def info(self):
        return f"{self.title} by {self.author} - {self.pages} sayfa, {self.read_pages} sayfa okundu"


class BankAccount:
    def __init__(self, acc_no, owner, balance=0):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"+{amount} TL")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"-{amount} TL")
        else:
            raise ValueError("Insufficient balance")

    def info(self):
        last = self.history[-1] if self.history else "No transactions"
        return f"Bakiye: {self.balance} TL, Son işlem: {last}"


import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_salary(self):
        return self.salary

    def info(self):
        return f"{self.name} - {self.department} Departmanı, Maaş: {self.calculate_salary()} TL"


class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def calculate_salary(self):
        return self.salary + self.team_size * 100

    def info(self):
        return f"{self.name} - {self.department} Departmanı, Yönetici, Ekip: {self.team_size} kişi, Maaş: {self.calculate_salary()} TL"


class Engineer(Employee):
    def __init__(self, name, salary, department, project_count):
        super().__init__(name, salary, department)
        self.project_count = project_count

    def calculate_salary(self):
        return self.salary + self.project_count * 200

    def info(self):
        return f"{self.name} - {self.department} Departmanı, Mühendis, Projeler: {self.project_count}, Maaş: {self.calculate_salary()} TL"


class BookItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed_by = None

    def is_available(self):
        return self.borrowed_by is None


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if len(self.borrowed_books) < 3 and book.is_available():
            self.borrowed_books.append(book)
            book.borrowed_by = self
        else:
            raise ValueError("Cannot borrow book")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.borrowed_by = None


class Library:
    def __init__(self, books):
        self.books = books

    def available_books(self):
        return [b for b in self.books if b.is_available()]


class Device:
    def __init__(self, location):
        self.location = location
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False


class Light(Device):
    pass


class Thermostat(Device):
    def __init__(self, location, temperature):
        super().__init__(location)
        self.temperature = temperature


class SecurityCamera(Device):
    pass


class HomeSystem:
    def __init__(self, devices):
        self.devices = devices

    def status(self):
        return [(d.location, d.on) for d in self.devices]


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
        else:
            raise ValueError("Insufficient stock")


class Cart:
    def __init__(self):
        self.items = {}
        self.discount = 0

    def add(self, product, qty):
        product.reduce_stock(qty)
        self.items[product] = self.items.get(product, 0) + qty

    def apply_discount(self, percent):
        self.discount = percent

    def total(self):
        total = sum(p.price * q for p, q in self.items.items())
        return total * (1 - self.discount / 100)


class CSVAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load(self):
        try:
            with open(self.file_path, newline="") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def clean(self):
        self.data = [row for row in self.data if all(row.values())]

    def stats(self, column):
        nums = [float(row[column]) for row in self.data if row[column].replace('.', '', 1).isdigit()]
        return {
            "mean": statistics.mean(nums),
            "median": statistics.median(nums),
            "stdev": statistics.stdev(nums) if len(nums) > 1 else 0
        }