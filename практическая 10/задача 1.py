print("Кодовый замок")

password = 4590

while True:
    ask = int(input("Введите пароль: "))
    if ask == password:
        print("Доступ разрешен")
        break
    if ask != password:
        print("Ошибка. Попробуйте ещё раз")