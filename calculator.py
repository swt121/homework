import tkinter as tk

def calculator():

    calc_state = {
        "first_num": 0,
        'second_num': 0,
    }

    def click_btn(number):
        current = current_num.get()
        current_num.delete(0, tk.END)
        current_num.insert(0, str(current) + str(number))

    def clear_btn():
        current_num.delete(0, tk.END)

    def div_btn():
        try:
            calc_state["first_num"] = int(first_num.get())
            calc_state['second_num'] = int(second_num.get())
            result.delete(0, tk.END)
            result.insert(0, calc_state["first_num"] // calc_state['second_num'])
        except ZeroDivisionError:
            result.delete(0, tk.END)
            result.insert(0, 'You cant divide by 0')
        except ValueError:
            result.delete(0, tk.END)
            result.insert(0, 'Error')

    def mod_btn():
        try:
            calc_state["first_num"] = int(first_num.get())
            calc_state['second_num'] = int(second_num.get())
            result.delete(0, tk.END)
            result.insert(0, calc_state["first_num"] % calc_state['second_num'])
        except ValueError:
            result.delete(0, tk.END)
            result.insert(0, 'Error')

    def negative_btn():
        current = current_num.get()
        if current.startswith("-"):
            current = current[1:]
        else:
            current = "-" + current
        current_num.delete(0, tk.END)
        current_num.insert(0, current)

    def tab_btn():
        nonlocal current_num
        if current_num == first_num:
            current_num = second_num
        else:
            current_num = first_num
        current_num.focus()

    root = tk.Tk()
    root.title("Калькулятор")
    root.geometry("400x400")

    first_num = tk.Entry(root)
    first_num.grid(row=0, column=0, columnspan=2, padx=1, ipadx=10, ipady=10)

    second_num = tk.Entry(root)
    second_num.grid(row=0, column=2, columnspan=2, padx=1, ipadx=10, ipady=10)

    result = tk.Entry(root)
    result.grid(row=1,column=1, columnspan=2, padx=1, ipadx=10, ipady=10)

    current_num = first_num

    buttons = [
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('div', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('mod', 3, 3),
        ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('+/-', 4, 3),
        ('C', 5, 0), ('0', 5, 1),('tab', 5, 2)
    ]

    for (text, row, col) in buttons:
        if text == 'div':
            tk.Button(root, text=text, cursor='hand2', command=div_btn, width=10, height=2).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        elif text == 'mod':
            tk.Button(root, text=text, cursor='hand2', command=mod_btn, width=10, height=2).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        elif text == 'C':
            tk.Button(root, text=text, cursor='hand2', command=clear_btn, width=10, height=2).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        elif text == '+/-':
            tk.Button(root, text=text, cursor='hand2', command=negative_btn, width=10, height=2).grid(row=row, column=col,padx=5,
                                                                                    pady=5, sticky='nsew')
        elif text == 'tab':
            tk.Button(root, text=text, cursor='hand2', command=tab_btn).grid(row=row,column=col, padx=5, pady=5, sticky='nsew')
        else:
            tk.Button(root, text=text, cursor='hand2', command=lambda t=text: click_btn(t), width=10, height=2).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    for i in range(5):
        root.grid_columnconfigure(i, weight=1)
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()


calculator()