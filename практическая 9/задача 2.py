print("сколько ждать")

a = "Александра"
l = "Левон"

found_a = False

count = 0

ask = input("Введите имя человека: ")

while ask != l:
    ask = input("Введите имя человека: ")
    if ask == a:
        found_a = True
        continue
    elif ask == l:
        print(f"Между Александрой и Левоном {count} человек")
    elif ask != l and found_a == True:
        count += 1