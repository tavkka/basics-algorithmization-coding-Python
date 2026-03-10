name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
subjects = input("Ваши любимые предметы (через запятую): ")

#создание словаря
student = {
    "name": name,
    "age": age,
    "subjects": subjects
}

#вывод анкеты с красивым оформлением
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")