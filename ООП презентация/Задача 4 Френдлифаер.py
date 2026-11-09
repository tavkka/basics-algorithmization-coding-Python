class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp

butcher = Zombie("Мясник", 100)

input_damage = int(input("Введите значение урона: "))

hp_now = butcher.bite(input_damage)
print(f"Остаток здоровья: {hp_now}")