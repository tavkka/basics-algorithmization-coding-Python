number = int(input("Введите номер кармана (0-36): "))

if number < 0 or number > 36:
    print("ошибка ввода")
else:
    if number == 0:
        print("зеленый")
    elif 1 <= number <= 10:
        if number % 2 != 0:
            print("красный")
        else:
            print("черный")
    elif 11 <= number <= 18:
        if number % 2 != 0:
            print("черный")
        else:
            print("красный")
    elif 19 <= number <= 28:
        if number % 2 != 0:
            print("красный")
        else:
            print("черный")
    elif 29 <= number <= 36:
        if number % 2 != 0:
            print("черный")
        else:
            print("красный")