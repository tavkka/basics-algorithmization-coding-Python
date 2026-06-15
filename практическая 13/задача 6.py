print("Задача 6: Всё сразу 2")

numbers = [8, 9, 10, 11]

numbers[1] = 17

numbers.extend([4, 5, 6])

del numbers[0]

copy_numbers = numbers.copy()

numbers.extend(copy_numbers)

numbers.insert(3, 25)

print(numbers)