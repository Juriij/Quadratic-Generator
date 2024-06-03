import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


def setup(root):
    root.title("Welcome to Math")
    width = 1000
    height = 700
    root.geometry(f'{str(width)}x{str(height)}')


    # Title text
    fontObj = tkFont.Font(size=40)
    title = tk.Label(root, text="Quadratic Generator", 
                    height = 5, width = 40, font=fontObj)
    
 


    # Buttons 
    style = ttk.Style(root)
    style.configure("Custom.TButton",
                    font=("Helvetica", 14, "bold"),
                    foreground="black",    
                    background="#1E88E5",    
                    padding=10)

    style.map("Custom.TButton",
            focuscolor=[('!focus', 'None')],
            background=[('active', '#1565C0')])  



    eq_button = ttk.Button(root, text="Equation", style="Custom.TButton")
    ineq_button = ttk.Button(root, text="Inequality", style="Custom.TButton")
       

    title.pack()
    eq_button.place(x=(width//2)-185,     y=(height//2)-50)
    ineq_button.place(x=(width//2)+35,   y=(height//2)-50)

