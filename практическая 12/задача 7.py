print("Задача 7: Ручной поиск индекса")

numbers = [10, 20, 30, 40, 50]
num = int(input("Введите число: "))
found_num = False

for i in range(len(numbers)):
    if num == numbers[i]:
        print(f"Индекс вашего числа в списке: {i}")
        found_num = True
        break

if found_num == False:
    print("Такого числа нет")