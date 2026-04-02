import math

num1 = float(input("Введите x1: "))
num2 = float(input("Введите x2: "))
num3 = float(input("Введите y1: "))
num4 = float(input("Введите y2: "))

p = math.sqrt(pow(num1 - num2, 2) + pow(num3 - num4, 2))
print(f"Евклидово расстояние между двумя точками равно {p}")