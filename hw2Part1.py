import hashlib
import uuid
from tkinter import *
from tkinter.messagebox import showinfo

def create_password():
    global hashed_password
    global abc
    abc = uuid.uuid4()
    hashed_password = hashlib.md5((create_pass.get() + str(abc)).encode()).digest()
    create_pass.delete(0, END)

def check():
    check_password = check_pass.get()
    if hashed_password == hashlib.md5((check_password + str(abc)).encode()).digest():
        check_pass.delete(0, END)
        showinfo(title='Победа', message='Пароль верный')
    else:
        check_pass.delete(0, END)
        showinfo(title='Неудача', message='Пароль неверный')

hashed_password = None
abc = None

root = Tk()
root.title('Проверка пароля')
root.geometry('400x400')

create_pass = Entry()
create_pass.grid(row=0, column=0)

create_btn = Button(text='Создать пароль', command=create_password)
create_btn.grid(row=0, column=1)

check_pass = Entry()
check_pass.grid(row=1, column=0, pady=20)

check_btn = Button(text='Проверить пароль', command=check)
check_btn.grid(row=1, column=1, pady=20)

root.mainloop()
