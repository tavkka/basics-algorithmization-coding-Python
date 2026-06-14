print("Задача 8: Обмен значений")

numbers = [213, 32, 42, 56, 12]
min_index = 0

for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(numbers)