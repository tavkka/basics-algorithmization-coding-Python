print("Задача 3: Windows OS")

files = input("Введите имя файла: ")
parts = files.split('\\')

for part in parts:
    print(part)