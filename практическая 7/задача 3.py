print("=" * 49)
print("=", " " * 10, "ИНТЕРАКТИВНОЕ МЕНЮ КАФЕ", " " * 10, "=")
print("=" * 49)

drink = int(input("Введите номер напитка (1-5): "))
count = int(input("Введите количество напитков: "))

match drink:
    case 1:
        drinks = "Кофе ☕"
        price = 120
        total = price * count
    case 2:
        drinks = "Чай 🍵"
        price = 80
        total = price * count
    case 3:
        drinks = "Сок 🧃"
        price = 100
        total = price * count
    case 4:
        drinks = "Вода 💧"
        price = 50
        total = price * count
    case 5:
        drinks = "Лимонад 🥤"
        price = 90
        total = price * count
    case _:
        print("Введена некорректная позиция.")

print("=" * 49)
print("=", " " * 14, "КВИТАНЦИЯ КАФЕ", " " * 15, "=")
print("=" * 49)

print(f"Товар: {drinks}")
print(f"Цена за порцию: {price}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
