print("Проверка на чётность каждого числа")

check = 0

for i in range(1, 11):
    num = int(input("Введите целое число: "))
    if num % 2 == 0:
        check += 1
        if check == 10:
            final = "YES"
    else:
        final = "NO"

print(final)