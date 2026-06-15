print("Задача 4: Корректный IP-адрес")

ip = input("Введите ip адрес: ")
parts = ip.split('.')

if len(parts) != 4:
    print("НЕТ")
else:
    valid = True
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                valid = False
                break
        except ValueError:
            valid = False
            break

    if valid == True:
        print("ДА")
    else:
        print("НЕТ")