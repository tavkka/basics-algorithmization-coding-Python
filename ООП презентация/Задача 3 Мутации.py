class Monster:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp

    def mutate(self):
        self.power += 5
        print(f"{self.name} мутирует! Сила увеличена!\n⚔️: {self.power}")

    def rest(self):
        self.hp += 10
        print(f"{self.name} отдыхает в склепе! Здоровье восстановлено!\n❤️: {self.hp}")

lucan = Monster("Люкан", 15, 90)
lucan.mutate()
lucan.rest()