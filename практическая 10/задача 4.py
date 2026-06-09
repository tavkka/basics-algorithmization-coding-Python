print("Кассовый аппарат")

price = 0

while True:
    ask = int(input("Введите цену товара (или 0 чтобы выйти): "))
    if ask == 0:
        break
    if ask <= -1:
        print("Ошибка цены")
        continue
    if ask >= 1:
        price += ask

print(f"Цена ваших покупок {price} руб.")
if price >= 1000:
    discount = price * 0.1
    with_discount = int(price - discount)
    print(f"Итоговая сумма покупок со скидкой {with_discount} руб.")