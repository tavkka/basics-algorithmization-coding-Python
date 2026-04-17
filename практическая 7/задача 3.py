print("=" * 49)
print("=", " " * 10, "ИНТЕРАКТИВНОЕ МЕНЮ КАФЕ", " " * 10, "=")
print("=" * 49)

drink = input("Введите номер напитка (1-5): ")

try:
    drink = int(drink)
except ValueError:
    print("Введено некорректное значение")
    exit()

match drink:
    case 1:
        