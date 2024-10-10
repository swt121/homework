from tkinter import *
from tkinter import messagebox

class Login(Frame):
    def __init__(self, app, master):
        super().__init__(master)
        self.app = app

        # создание экрана для входа в аккаунт
        Label(self, text='Войдите в свой аккаунт', font=("Arial", 16)).pack(pady=20)

        Label(self, text='Имя пользователя').pack(pady=5)

        self.username_entry = Entry(self)
        self.username_entry.pack(pady=5)

        Label(self, text="Пароль").pack(pady=5)

        self.password_entry = Entry(self, show='*')
        self.password_entry.pack(pady=5)

        Button(self, text="Войти", command=self.login).pack(pady=10)
        Button(self, text="Регистрация", command=self.app.show_register).pack(pady=5)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not password or not username:
            return messagebox.showwarning('Ошибка', 'Для регистрации нужно заполнить все поля')

        user = self.app.data.get_user(username, password)

        if user:
            self.app.current_user = user
            self.app.show_chat()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")