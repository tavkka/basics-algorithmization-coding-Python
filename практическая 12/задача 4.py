print("Задача 4: Ручной подсчет")

marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
two = 0
five = 0

for mark in marks:
    if mark == 2:
        two += 1
    if mark == 5:
        five += 1
        
print(f"Двоек всего: {two}\nПятёрок всего: {five}")