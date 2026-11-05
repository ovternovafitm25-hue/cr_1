import math

# ФУНКЦІЯ ОБЧИСЛЕННЯ ФАКТОРІАЛУ
def factorial(n):
    if n < 0:
        return "Факторіал для від'ємних чисел не визначений"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# ПЛОЩА ГЕОМЕТРИЧНИХ ФІГУР
def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height

# ГЕНЕРАТОР ПАРНИХ ЧИСЕЛ
def even_generator(limit):
    for number in range(0, limit + 1):
        if number % 2 == 0:
            yield number

# ВЛАСНИЙ ІТЕРАТОР
class NumberIterator:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_number:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

# ОСНОВНА ПРОГРАМА
# Типи даних
integer_value = 10
float_value = 5.75
string_value = "Python"
bool_value = True

print("Типи даних:")
print("Ціле число:", integer_value)
print("Дійсне число:", float_value)
print("Рядок:", string_value)
print("Логічне:", bool_value)

# Факторіал
number = 5
print("\nФакторіал числа", number, "=", factorial(number))

# Умовна конструкція
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

# Геометричні обчислення
radius = 4
length = 5
width = 8
base = 6
height = 7

print("\nГеометричні фігури:")
print("Площа кола =", round(circle_area(radius), 2))
print("Площа прямокутника =", rectangle_area(length, width))
print("Площа трикутника =", triangle_area(base, height))

# Список
numbers_list = [3, 7, 1, 9, 5]
print("\nСписок:", numbers_list)

# Кортеж
coordinates = (10, 20)
print("Кортеж:", coordinates)

# Словник
student = {
    "Ім'я": "Олена",
    "Група": "КБ-21",
    "Середній бал": 91
}
print("Словник:", student)

# Цикл for
print("\nЕлементи списку:")
for item in numbers_list:
    print(item)

# Цикл while
print("\nЛічильник:")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# Робота генератора
print("\nПарні числа (генератор):")
for num in even_generator(10):
    print(num, end=" ")

print()

# Робота ітератора
print("\nЧисла (ітератор):")
iterator = NumberIterator(5)

for num in iterator:
    print(num)

print("\nПрограма завершена.")
