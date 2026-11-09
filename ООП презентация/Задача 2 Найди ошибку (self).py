class Monster:
    def __init__(self, name):
        self.name = name
        
# У метода необходимо добавить атрибут self, чтобы у метода был доступ к информации о созданном монстре и его данным
    def introduce(self):
        print(f"Я {self.name}, и я хочу кушать!")

m = Monster("Упырь")
m.introduce()