import json
import os
from UsersPart import Users
from ChatsPart import Chats

class Data:
    def __init__(self, file='data.json'):
        self.file = file
        self.users = []
        self.chats = []

        self.load_data()

    def save_data(self):
        data = {'users': [i.to_data() for i in self.users],
                'chats': [j.to_data() for j in self.chats]}

        with open(self.file, 'w', encoding='utf-8') as n:
            json.dump(data, n, ensure_ascii=False, indent=4)

    def load_data(self):
        if not os.path.exists(self.file): # если файла не существует, то мы его создаем
            self.chats.append(Chats('Животные'))
            self.chats.append(Chats('Учеба'))
            # создаем чаты
            self.save_data()
            # сохраняем данные с помощью функции
        with open(self.file, 'r', encoding='utf-8') as n:
            data = json.load(n)
            self.users = [Users.from_data(i) for i in data.get('users',[])]
            self.chats = [Chats.from_data(j) for j in data.get('chats', [])]

    def get_user(self, username, password):
        for i in self.users:
            if i.username == username and i.password == password:
                return i
        return None

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def get_chat_name(self):
        return [i.name for i in self.chats]

    def get_chat(self, name):
        for i in self.chats:
            if i.name == name:
                return i
        return None

    def user_exists(self, username):
        for i in self.users:
            if i.username == username:
                return True

        return False