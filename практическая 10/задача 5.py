print("Банкомат")

balance = 1000

while True:
    ask = int(input("Введите 1 чтобы узнать баланс, 2 чтобы снять 100 рублей, 3 чтобы положить 100 рублей, 4 чтобы выйти: "))

    if ask == 1:
        print(f"Ваш текущий баланс {balance}")

    elif ask == 2:
        print(f"Ваш текущий баланс {balance}")

        if balance >= 100:
            balance = balance - 100
            print("Операция выполнена успешно")
            print(f"Ваш текущий баланс {balance}")
        else:
            print("Недостаточно средств")

    elif ask == 3:
        balance = balance + 100
        print("Операция выполнена успешно")
        print(f"Ваш текущий баланс {balance}")

    elif ask == 4:
        print("До свидания")
        break

    else:
        print("Неверная команда")