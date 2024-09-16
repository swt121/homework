import tkinter as tk
from tkinter import messagebox
import hashlib
import uuid

def generate_salt():
    return str(uuid.uuid4()).encode()

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

users = {}

def register_user(username, password):
    if username in users:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
        return
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    users[username] = (hashed_password, salt)
    messagebox.showinfo("Успех", "Регистрация прошла успешно!")

def check_login(username, password):
    print(users)
    if username not in users:
        messagebox.showerror("Ошибка", "Пользователь не найден!")
        return
    hashed_password, salt = users[username]
    if hashed_password == hash_password(password, salt):
        messagebox.showinfo("Успех", "Логин успешен!")
    else:
        messagebox.showerror("Ошибка", "Неверный пароль!")

def register():
    username = entry_username.get()
    register_user(username, entry_password.get())

def login():
    username = entry_username.get()
    check_login(username, entry_password.get())

root = tk.Tk()
root.title("Проверка пароля")
root.geometry('400x400')

tk.Label(root, text="Логин:").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Пароль:").grid(row=1, column=0)
entry_password = tk.Entry(root)
entry_password.grid(row=1, column=1)

tk.Button(root, text="Регистрация", command=register).grid(row=2, column=0, pady=10)
tk.Button(root, text="Логин", command=login).grid(row=2, column=1, pady=10)

root.mainloop()
