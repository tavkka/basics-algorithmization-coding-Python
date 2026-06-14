print("Задача 6: Палиндром")

word = input("Введите слово: ")
symbols = list(word)
reverse = symbols[::-1]

if symbols == reverse:
    print("Это палиндром")
else:
    print("Не палиндром")