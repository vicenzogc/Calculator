import tkinter as tk
from tkinter import messagebox

# Funções
def somar():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        resultado = valor1 + valor2
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display_error("Erro: Os valores devem ser números.")

def subtrair():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        resultado = valor1 - valor2
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display_error("Erro: Os valores devem ser números.")

def multiplicar():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        resultado = valor1 * valor2
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display_error("Erro: Os valores devem ser números.")

def dividir():
    try:
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        if valor2 == 0:
            raise ZeroDivisionError
        resultado = valor1 / valor2
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ZeroDivisionError:
        display_error("Erro: Divisão por zero.")
    except ValueError:
        display_error("Erro: Os valores devem ser números.")

def calcular_porcentagem():
    try:
        valor = float(entry1.get())
        porcentagem = float(entry2.get())
        resultado = valor * (porcentagem / 100)
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except ValueError:
        display_error("Erro: Os valores devem ser números.")

def limpar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    display.delete(0, tk.END)

def display_error(message):
    messagebox.showerror("Erro", message)

# Configuração da interface do usuário
root = tk.Tk()
root.title("Calculadora")

frame = tk.Frame(root)
frame.pack(pady=10)

# Entradas
tk.Label(frame, text="Valor 1:").grid(row=0, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

tk.Label(frame, text="Valor 2:").grid(row=1, column=0)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

# Display
display = tk.Entry(frame, width=30, borderwidth=2, relief="sunken")
display.grid(row=2, columnspan=2, pady=5)

# Botões
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Somar", command=somar).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtrair", command=subtrair).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiplicar", command=multiplicar).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="Dividir", command=dividir).grid(row=0, column=3, padx=5, pady=5)
tk.Button(button_frame, text="Porcentagem", command=calcular_porcentagem).grid(row=0, column=4, padx=5, pady=5)
tk.Button(button_frame, text="Limpar", command=limpar).grid(row=0, column=5, padx=5, pady=5)

root.mainloop()
