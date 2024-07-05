import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<Key - F4>', return_pressed) #Key deve ser com "K" maiusculo


btn.focus()
btn.pack(expand=True)

root.mainloop()
