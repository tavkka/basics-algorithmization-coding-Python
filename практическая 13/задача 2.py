print("Задача 2: Символы всех строк")

n = int(input("Введите количество строк: "))
symbols = []

for i in range(n):
    line = input("Введите что-нибудь: ")
    symbols.extend(line)

print(symbols)
