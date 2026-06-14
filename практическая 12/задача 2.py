print("Задача 2: Анализ цен")

prices = [1500, 500, 2000, 3500, 1000, 4500]
summa = sum(prices)

print(f"Самый дорогой товар: {max(prices)}")
print(f"Самый дешёвый товар: {min(prices)}")
print(f"Общая стоимость товаров: {summa}")
print(f"Средняя цена товара: {summa / len(prices)}")