print("Знакочередующаяся сумма")

n = int(input("Введите натуральное число: "))

number = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        number = number - i
    else:
        number = number + i
print(f"Знакочередующаяся сумма равна: {number}")
