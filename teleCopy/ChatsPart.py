class Chats:
    def __init__(self, name):
        self.name = name
        self.messages = [] # Список кортежей вида: (name, message)

    def to_data(self):
        return {'name': self.name,
                'messages': self.messages}

    @staticmethod
    def from_data(data):
        chat = Chats(data['name'])
        chat.messages = data.get('messages', [])
        return chat

    def add_message(self, username, message):
        return self.messages.append((username, message))