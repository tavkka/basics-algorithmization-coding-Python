print("=" * 27)
print("СИСТЕМА РЕЙТИНГА ПРОДУКТОВ")
print("=" * 27)

num = input("Введите число (1-10): ")
try:
    num = int(num)
except ValueError:
    print("Введено некорректное число")
    exit()

match num:
    case 1 | 2 | 3:
        result = "Плохой продукт! ❌ Не рекомендую."
    case 4 | 5 | 6:
        result = "Средний продукт! 😐 Можно попробовать."
    case 7 | 8 | 9:
        result = "Отличный продукт! ☀️ Настоятельно рекомендую!"
    case _:
        print("Число должно быть от 1 до 10")

print(f"Рейтинг {num} --> {result}")