class Monster:
    def __init__(self, name="Неизвестный монстр", hp=100, dmg=50):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def show_info(self):
        print(f"{self.name}")
        print(f"❤️: {self.hp}")
        print(f"⚔️: {self.dmg}")

gargylia = Monster("Горгулья", 120, 18)
gargylia.show_info()