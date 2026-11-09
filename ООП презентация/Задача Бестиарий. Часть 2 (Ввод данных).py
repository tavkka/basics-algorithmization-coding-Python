class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

input_monster1 = input("Введите имя, hp и dmg вашего монстра через пробел: ")
input_monster2 = input("Введите имя, hp и dmg вашего монстра через пробел: ")

monster1 = input_monster1.split()
monster2 = input_monster2.split()

m1 = Monster(name=monster1[0], hp=int(monster1[1]), dmg=int(monster1[2]))
m2 = Monster(name=monster2[0], hp=int(monster2[1]), dmg=int(monster2[2]))