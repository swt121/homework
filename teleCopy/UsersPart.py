class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_data(self):
        return {'username': self.username,
                'password': self.password}

    @staticmethod
    def from_data(data):
        return Users(data['username'], data['password'])