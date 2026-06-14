print("Задача 3: Изменение списка")

users = ['Admin', 'Guest', 'User', 'Bot']

users[2] = 'Moderator'
users[-1] = 'SuperAdmin'
users.append('Newbie')

print(f"Итоговый список: {users}")