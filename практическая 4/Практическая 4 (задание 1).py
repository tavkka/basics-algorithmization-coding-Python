import math

num1 = float(input("Введите действительное число: "))
num2 = float(input("Введите действительное число: "))

summa = math.floor(num1) + math.ceil(num2)
print(f"Сумма ваших чисел = {summa}")