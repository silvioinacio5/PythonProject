import math
import tkinter as tk
from tkinter import messagebox

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        if a == 0:
            messagebox.showerror("Error", "O valor de A deve ser diferente de zero.")
            return
        
        equation = f"{a}X² {'+ ' if b >= 0 else ''}{b}X {'+ ' if c >= 0 else ''}{c} = 0"
        lbl_equation.config(text=equation)

        delta = b**2 - 4*a*c
        lbl_delta.config(text=f"Δ = {delta:.2f}")

        if delta < 0:
            lbl_result_x1.config(text="X1 = No Solution!")
            lbl_result_x2.config(text="X2 = No Solution!")
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2 * a)
            x2 = (-b - sqrt_delta) / (2 * a)
            lbl_result_x1.config(text=f"X1 = {x1:.2f}")
            lbl_result_x2.config(text=f"X2 = {x2:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, insira valores numéricos válidos.")

# Create the main window
root = tk.Tk()
root.title("Solver for Quadratic Equations")

# Input fields
tk.Label(root, text="Valor de A:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Valor de B:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Valor de C:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Buttons
btn_solve = tk.Button(root, text="Solve", command=solve_quadratic)
btn_solve.grid(row=3, column=0, columnspan=2, pady=10)

# Output labels
lbl_equation = tk.Label(root, text="", font=("Arial", 12))
lbl_equation.grid(row=4, column=0, columnspan=2, pady=5)

lbl_delta = tk.Label(root, text="", font=("Arial", 12))
lbl_delta.grid(row=5, column=0, columnspan=2, pady=5)

lbl_result_x1 = tk.Label(root, text="", font=("Arial", 12))
lbl_result_x1.grid(row=6, column=0, columnspan=2, pady=5)

lbl_result_x2 = tk.Label(root, text="", font=("Arial", 12))
lbl_result_x2.grid(row=7, column=0, columnspan=2, pady=5)

# Run the main loop
root.mainloop()
