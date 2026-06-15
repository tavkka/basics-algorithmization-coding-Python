print("Задача 5: Количество совпадающих пар")

num = input("Введите числа (разделённые пробелом): ")
parts = num.split()
numbers = []

for part in parts:
    number = int(part)
    numbers.append(number)

pairs = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pairs += 1

print(f"Количество пар: {pairs}")