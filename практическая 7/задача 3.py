print("=" * 49)
print("=", " " * 10, "ИНТЕРАКТИВНОЕ МЕНЮ КАФЕ", " " * 10, "=")
print("=" * 49)

drink = input("Введите номер напитка (1-5) или название с маленькой буквы: ")

try:
    count = int(input("Введите количество напитков: "))
except ValueError:
    print("Введено некорректное значение")
    exit()

match drink:
    case "1" | "кофе":
        drinks = "Кофе ☕"
        price = 120
        total = price * count
    case "2" | "чай":
        drinks = "Чай 🍵"
        price = 80
        total = price * count
    case "3" | "сок":
        drinks = "Сок 🧃"
        price = 100
        total = price * count
    case "4" | "вода":
        drinks = "Вода 💧"
        price = 50
        total = price * count
    case "5" | "лимонад":
        drinks = "Лимонад 🥤"
        price = 90
        total = price * count
    case _:
        print("Введена некорректная позиция.")
        exit()

discount = input("Введите код скидки (SKIDKA1 или SKIDKA2) или оставьте пустым: ")

match discount:
    case "SKIDKA1":
        discount_quantity = total * 0.1
        discount_final = "Скидка 10%"
    case "SKIDKA2":
        discount_quantity = total * 0.2
        discount_final = "Скидка 20%"
    case "":
        discount_quantity = 0
        discount_final = "Нет скидки"
    case _:
        print("Данный код не существует")
        discount_quantity = 0
        discount_final = "Нет скидки"

match count:
    case 1:
        portions = "порция"
    case 2 | 3 | 4:
        portions = "порции"
    case _:
        portions = "порций"

totally_total = total - discount_quantity

print("=" * 49)
print("=", " " * 14, "КВИТАНЦИЯ КАФЕ", " " * 15, "=")
print("=" * 49)

print(f"Товар: {drinks}")
print(f"Цена за порцию: {price} руб.")
print(f"Количество: {count} {portions}")
print(f"Сумма: {total} руб.")
print(f"{discount_final} по коду {discount}: -{discount_quantity} руб.")

print("=" * 49)
print(f"К оплате: {totally_total} руб.")
print("=" * 49)
