import math

corner = int(input("Введите угол: "))
corner = math.radians(corner)

result = math.sin(corner) + math.cos(corner) + math.pow(math.tan(corner), 2)
print("Результат выражения: ", result)