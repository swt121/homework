from tkinter import *
from tkinter import messagebox
from UsersPart import Users

class Register(Frame):
    def __init__(self, app, master):
        super().__init__(master)
        self.app = app

        Label(self, text="Регистрация в Чат Приложение", font=("Arial", 16)).pack(pady=20)

        Label(self, text="Имя пользователя").pack(pady=5)
        self.username_entry = Entry(self)
        self.username_entry.pack(pady=5)

        Label(self, text="Пароль").pack(pady=5)
        self.password_entry = Entry(self, show='*')
        self.password_entry.pack(pady=5)

        Button(self, text="Зарегистрироваться", command=self.register).pack(pady=10)
        Button(self, text="Назад", command=self.app.show_login).pack(pady=5)

    def register(self, **kwargs):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Предупреждение", "Заполните все поля")
            return

        if self.app.data.user_exists(username):
            messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует")
            return

        new_user = Users(username, password)
        self.app.data.add_user(new_user)
        messagebox.showinfo("Победа", "Регистрация прошла успешно!")
        self.app.show_login()