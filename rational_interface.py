import tkinter as tk
from tkinter import ttk
from rational import Rational

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Вычисление рациональной дроби")
        self.root.geometry('570x230')
        self.root.resizable(False, False)

        # Радиокнопки для выбора между целым и дробным числом
        self.num_type = tk.StringVar(value="fraction")

        self.fraction_radio = tk.Radiobutton(root, text="Дробное", variable=self.num_type, value="fraction",
                                             command=self.update_inputs)
        self.fraction_radio.grid(row=0, column=1)

        self.whole_radio = tk.Radiobutton(root, text="Целое", variable=self.num_type, value="integer", command=self.update_inputs)
        self.whole_radio.grid(row=1, column=1)


        # Поля для первого числа
        self.n1_label = tk.Label(root, text="Первое число (целое или числитель)")
        self.n1_label.grid(row=0, column=0)
        self.n1_entry = tk.Entry(root)
        self.n1_entry.grid(row=1, column=0)

        self.d1_label = tk.Label(root, text="Знаменатель (только для дроби)")
        self.d1_label.grid(row=2, column=0)
        self.d1_entry = tk.Entry(root)
        self.d1_entry.grid(row=3, column=0)

        # Поля для второго числа
        self.n2_label = tk.Label(root, text="Второе число (целое или числитель)")
        self.n2_label.grid(row=0, column=2)
        self.n2_entry = tk.Entry(root)
        self.n2_entry.grid(row=1, column=2)

        self.d2_label = tk.Label(root, text="Знаменатель (только для дроби)")
        self.d2_label.grid(row=2, column=2)
        self.d2_entry = tk.Entry(root)
        self.d2_entry.grid(row=3, column=2)

        # Выбор операции
        self.operation_label = tk.Label(root, text="Операция")
        self.operation_label.grid(row=4, column=1)
        self.operation_combobox = ttk.Combobox(root, values=["+", "-", "*", "/"], state='readonly')
        self.operation_combobox.grid(row=5, column=1)

        # Кнопка вычисления
        self.calculate_button = tk.Button(root, text="Вычислить", command=self.calculate)
        self.calculate_button.grid(row=6, column=1, pady=10)

        # Результат
        self.result_label = tk.Label(root, text="Результат")
        self.result_label.grid(row=7, column=1)
        self.result_entry = tk.Entry(root, state='readonly')
        self.result_entry.grid(row=8, column=1)

    def update_inputs(self):
        """Обновляет видимость полей ввода знаменателя в зависимости от выбора целого или дробного числа."""
        if self.num_type.get() == "integer":
            self.d1_entry.grid_remove()
            self.d2_entry.grid_remove()
        else:
            self.d1_entry.grid()
            self.d2_entry.grid()

    def calculate(self):
        """Вычисляет результат в зависимости от введённых значений и выбранной операции."""
        global result
        try:
            if self.num_type.get() == "integer":
                n1 = int(self.n1_entry.get())
                n2 = int(self.n2_entry.get())
                fraction1 = Rational(n1, 1)  # Представляем целое число как дробь со знаменателем 1
                fraction2 = Rational(n2, 1)
            else:
                n1 = int(self.n1_entry.get())
                d1 = int(self.d1_entry.get())
                n2 = int(self.n2_entry.get())
                d2 = int(self.d2_entry.get())
                fraction1 = Rational(n1, d1)
                fraction2 = Rational(n2, d2)

            operation = self.operation_combobox.get()

            if operation == "+":
                result = fraction1 + fraction2
            elif operation == "-":
                result = fraction1 - fraction2
            elif operation == "*":
                result = fraction1 * fraction2
            elif operation == "/":
                result = fraction1 / fraction2

            self.display_result(result)

        except ValueError:
            self.result_entry.config(state='normal')
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Ошибка")
            self.result_entry.config(state='readonly')

    def display_result(self, result):
        """Отображает результат, если он целый, выводит как целое число, иначе как дробь."""
        self.result_entry.config(state='normal')
        self.result_entry.delete(0, tk.END)

        if result.d == 1:  # Если знаменатель равен 1, выводим как целое число
            self.result_entry.insert(0, str(result.n))
        else:
            self.result_entry.insert(0, f'{result.n} / {result.d}')

        self.result_entry.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

