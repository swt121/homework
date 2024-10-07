import tkinter as tk
from tkinter import ttk
from rational import Rational

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Вычисление рациональной дроби")

        self.n1_label = tk.Label(root, text="Первое выражение")
        self.n1_label.grid(row=0, column=0)
        self.n1_entry = tk.Entry(root)
        self.n1_entry.grid(row=1, column=0)

        self.d1_label = tk.Label(root, text="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        self.d1_label.grid(row=2, column=0)
        self.d1_entry = tk.Entry(root)
        self.d1_entry.grid(row=3, column=0)

        self.n2_label = tk.Label(root, text="Второе выражение")
        self.n2_label.grid(row=0, column=2)
        self.n2_entry = tk.Entry(root)
        self.n2_entry.grid(row=1, column=2)

        self.d2_label = tk.Label(root, text="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        self.d2_label.grid(row=2, column=2)
        self.d2_entry = tk.Entry(root)
        self.d2_entry.grid(row=3, column=2)

        self.operation_label = tk.Label(root, text="Операция")
        self.operation_label.grid(row=1, column=1)
        self.operation_combobox = ttk.Combobox(root, values=["+", "-", "*", "/"],state='readonly')
        self.operation_combobox.grid(row=2, column=1)

        self.calculate_button = tk.Button(root, text="Вычислить", command=self.calculate)
        self.calculate_button.grid(row=4, column=1)

        self.result_n_label = tk.Label(root, text="Результат")
        self.result_n_label.grid(row=5, column=1)
        self.result_n_entry = tk.Entry(root, state='readonly')
        self.result_n_entry.grid(row=6, column=1)

        self.result_d_label = tk.Label(root, text="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
        self.result_d_label.grid(row=7, column=1)
        self.result_d_entry = tk.Entry(root, state='readonly')
        self.result_d_entry.grid(row=8, column=1)

    def calculate(self):
        global result
        try:
            n1 = int(self.n1_entry.get())
            d1 = int(self.d1_entry.get())
            n2 = int(self.n2_entry.get())
            d2 = int(self.d2_entry.get())
            operation = self.operation_combobox.get()

            fraction1 = Rational(n1, d1)
            fraction2 = Rational(n2, d2)

            if operation == "+":
                result = fraction1 + fraction2
            elif operation == "-":
                result = fraction1 - fraction2
            elif operation == "*":
                result = fraction1 * fraction2
            elif operation == "/":
                result = fraction1 / fraction2

            self.result_n_entry.config(state='normal')
            self.result_n_entry.delete(0, tk.END)
            self.result_n_entry.insert(0, str(result.n))
            self.result_n_entry.config(state='readonly')

            self.result_d_entry.config(state='normal')
            self.result_d_entry.delete(0, tk.END)
            self.result_d_entry.insert(0, str(result.d))
            self.result_d_entry.config(state='readonly')

        except ValueError:
            self.result_n_entry.config(state='normal')
            self.result_n_entry.delete(0, tk.END)
            self.result_n_entry.insert(0, "Ошибка")
            self.result_n_entry.config(state='readonly')

            self.result_d_entry.config(state='normal')
            self.result_d_entry.delete(0, tk.END)
            self.result_d_entry.insert(0, "Ошибка")
            self.result_d_entry.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
