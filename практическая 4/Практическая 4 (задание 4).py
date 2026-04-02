students = int(input("Введите количество школьников: "))
mandarines = int(input("Введите количество мандаринов: "))

each = mandarines // students
ostatok = mandarines % students

print(f"Каждому достанется {each} мандаринов")
print(f"В корзине останется {ostatok} мандаринов")