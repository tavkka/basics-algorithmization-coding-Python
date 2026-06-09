print("Поиск максимума")

compare = 0

while True:
    ask = int(input("Введите любое целое число (или 0 чтобы остановиться): "))
    if ask == 0:
        break
    if compare < ask:
        compare = ask
print(compare)