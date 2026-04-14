pocket = int(input("Введите номер кармана: "))
if pocket == 0:
    print("Зелёный")
elif 1 <= pocket <= 10:
    if pocket % 2 == 1:
        print("Красный")
    else:
        print("Чёрный")
elif 11 <= pocket <= 18:
    if pocket % 2 == 1:
        print("Чёрный")
    else:
        print("Красный")
elif 19 <= pocket <= 28:
    if pocket % 2 == 1:
        print("Красный")
    else:
        print("Чёрный")
elif 29 <= pocket <= 36:
    if pocket % 2 == 1:
        print("Чёрный")
    else:
        print("Красный")
else:
    print("Ошибка! Введите число от 0 до 36")