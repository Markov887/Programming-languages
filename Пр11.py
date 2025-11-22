import tkinter as tk
from tkinter import ttk, messagebox, filedialog
window = tk.Tk()
window.title("Марков Артём Анатольевич")
window.geometry("600x400")
tab_control = ttk.Notebook(window)

#Калькулятор
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
ttk.Label(tab1, text="Калькулятор").pack(pady=10)
frame_calc = ttk.Frame(tab1)
frame_calc.pack(pady=10)
num1 = ttk.Entry(frame_calc, width=10)
num1.pack(side='left', padx=5)
operation = ttk.Combobox(frame_calc, values=['+', '-', '*', '/'], width=5)
operation.set('+')
operation.pack(side='left', padx=5)
num2 = ttk.Entry(frame_calc, width=10)
num2.pack(side='left', padx=5)
result_label = ttk.Label(tab1, text="Результат: ")
result_label.pack(pady=10)
def calculate():
    try:
        a = float(num1.get())
        b = float(num2.get())
        op = operation.get()
        if op == '+': res = a + b
        elif op == '-': res = a - b
        elif op == '*': res = a * b
        elif op == '/': res = a / b if b != 0 else 'Ошибка: деление на 0'
        result_label.config(text=f"Результат: {res}")
    except:
        messagebox.showerror("Ошибка", "Введите числа")
ttk.Button(tab1, text="=", command=calculate).pack(pady=5)

#Кнопка
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')
ttk.Label(tab2, text="Выберите варианты:").pack(pady=10)
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
ttk.Checkbutton(tab2, text="Первый", variable=var1).pack(pady=5)
ttk.Checkbutton(tab2, text="Второй", variable=var2).pack(pady=5)
ttk.Checkbutton(tab2, text="Третий", variable=var3).pack(pady=5)
def show_choice():
    choices = []
    if var1.get(): choices.append("Первый")
    if var2.get(): choices.append("Второй")
    if var3.get(): choices.append("Третий")
    text = "Вы выбрали: " + " ".join(choices) if choices else "Ничего не выбрано"
    messagebox.showwarning("Выбор", text)
ttk.Button(tab2, text="Показать выбор", command=show_choice).pack(pady=10)

#Текст
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Текст')
ttk.Label(tab3, text="Работа с текстом").pack(pady=10)
text_widget = tk.Text(tab3, width=40, height=10)
text_widget.pack(pady=10, padx=10, fill='both', expand=True)
frame_text = ttk.Frame(tab3)
frame_text.pack(pady=5)
def load_file():
    file = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, content)
        except:
            messagebox.showerror("Ошибка", "Не удалось загрузить файл")
def clear_text():
    text_widget.delete(1.0, tk.END)
ttk.Button(frame_text, text="Загрузить из файла", command=load_file).pack(side='left', padx=5)
ttk.Button(frame_text, text="Очистить", command=clear_text).pack(side='left', padx=5)
tab_control.pack(expand=1, fill='both')
window.mainloop()
