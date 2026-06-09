print("Задача про ведьмака")

cost = int(input("Введите цену ваших услуг: "))
moneta = 0

while cost >= 25:
    moneta += 1
    cost -= 25
while cost >= 10:
    moneta += 1
    cost -= 10
while cost >= 5:
    moneta += 1
    cost -= 5
while cost >= 1:
    moneta += 1
    cost -= 1
    
print(f"Минимальное количество трубуемых монет {moneta}")
