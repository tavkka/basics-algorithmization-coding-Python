import random

print("Угадай число")

secret = random.randint(1,10)
attempts = 1

print("Я загадала число от 1 до 10, у вас 3 попытки")

for i in range(1, 4):
    think = int(input("Какое число я загадала? "))
    attempts += 1

    if think == secret:
        print("Угадали!")
        break
    elif think > secret:
        print("Меньше")
    elif think < secret:
        print("Больше")
    if attempts > 3:
        print(f"Вы не угадали, число было {secret}")
        break