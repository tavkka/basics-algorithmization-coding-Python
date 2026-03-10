try:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    num1_int = int(num1)
    num2_int = int(num2)
    summa = num1_int + num2_int
    print("Сумма чисел: ", summa)
except ValueError:
    print("Ошибка! Введите целые числа.") #try находит ошибку а except её обрабатывает и выводит сообщение об ошибке