minutes = int(input("Введите минуты: "))
hours = minutes // 60
ostatok = minutes % 60

print(f"{minutes} минуты это {hours} часов и {ostatok} минут")