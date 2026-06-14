print("Задача 1: 12 месяцев")

for n in range(0, 13):
    for k in range(0, 13):
        for m in range(0, 13):
            if (n + k + m == 12) and (28 * n + 30 * k + 31 * m == 365):
                print(f"n = {n}, k = {k}, m = {m}")