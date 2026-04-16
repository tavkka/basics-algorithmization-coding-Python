num1 = input("Введите первое число: ")
operation = input("Введите операцию (+, -, *, /): ")
num2 = input("Введите второе число: ")
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Введены некорректные числа")
    exit()

match operation:
    case "+":
        result = num1 + num2
        print(f"{num1} {operation} {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} {operation} {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} {operation} {num2} = {result}")
    case "/":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            result = num1 / num2
            print(f"{num1} {operation} {num2} = {result}")
    case _:
        print("Неизвестная операция.")