month = int(input("Введите число месяца (1-12): "))
match month:
    case 12 | 1 | 2:
        print(f"Это {month} месяц, это зима ❄️")
    case 3 | 4 | 5:
        print(f"Это {month} месяц, это весна 🌸")
    case 6 | 7 | 8:
        print(f"Это {month} месяц, это лето ☀️")
    case 9 | 10 | 11:
        print(f"Это {month} месяц, это осень 🍂")
    case _:
        print("Введено некорректное число")
