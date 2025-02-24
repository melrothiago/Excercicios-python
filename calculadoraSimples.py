import tkinter as tk
import re

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

def calculate():
    try:
        expression = entry.get()
        if not expression:
            result = "Error"
        else:
            # Remove leading zeros from numbers in the expression
            expression = re.sub(r'\b0+(\d)', r'\1', expression)
            result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)
    entry.insert(0, "")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Entrada de texto
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x) if x != '=' else calculate() if entry.get() else None
    tk.Button(root, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão de limpar
tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=row_val, column=col_val)

# Iniciar o loop principal
root.mainloop()