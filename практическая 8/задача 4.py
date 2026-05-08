print("Популяция")

m = int(input("стартовое количество организмов: "))
p = int(input("среднесуточное увеличение в процентах: "))
n = int(input("количество дней для размножения: "))

population = m

for i in range(1, n + 1):
    population = population + population * p / 100
    print(f"{i} {population}")