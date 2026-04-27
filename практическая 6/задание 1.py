temperature = float(input("Введите вашу температуру: "))
pressure = int(input("Введите ваше давление: "))
pulse = int(input("Введите ваш пульс: "))
if (36 <= temperature <= 37) and (110 <= pressure <= 130) and (60 <= pulse <= 100):
    print("У вас нормальное состояние")
elif ((temperature < 35) or (temperature > 38)) or ((pressure < 105) or (pressure > 140)) or ((pulse < 55) or (pulse > 110)):
    print("Вам требуется врач")
else:
    print("У вас лёгкое недомогание")