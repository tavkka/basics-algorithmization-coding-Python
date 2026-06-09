print("Строго возрастающая последовательность чисел")

while True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    
    if num2 <= num1:
        print("Ошибка. Второе число должно быть больше")

        while True:
            num2 = int(input("Введите второе число ещё раз: "))
            if num2 > num1:
                break
                
    num3 = int(input("Введите третье число: "))
    if num3 <= num2:
        print("Ошибка. Третье число должно быть больше")

        while True:
            num3 = int(input("Введите третье число ещё раз: "))
            if num3 > num2:
                break

    if (num1 <= num2) and (num2 <= num3):
        print("Последовательность принята")
        break
