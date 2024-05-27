import functions as fun
import sympy as sp
import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()
 
# Setup
root.title("Welcome to Math")
width = 1000
height = 700
root.geometry(f'{str(width)}x{str(height)}')



# Title text
fontObj = tkFont.Font(size=40)
title = tk.Label(root, text="Quadratic Generator", 
                 height = 5, width = 40, font=fontObj)
title.pack()




root.mainloop()