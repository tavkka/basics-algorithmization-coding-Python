print("Задача 1: Список нечётных чисел")

n = int(input("Введите любое положительное число: "))
nums = []

for num in range(1, n + 1):
    if num % 2 == 1:
        nums.append(num)

print(*nums, sep=', ')