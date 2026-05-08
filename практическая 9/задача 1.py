n = int(input("Введите натуральное число: "))

number = 1

while number <= n:
    if (5 <= number <= 9) or (17 <= number <= 37) or (78 <= number <= 87):
        number += 1
        continue
    print(number)
    number += 1
