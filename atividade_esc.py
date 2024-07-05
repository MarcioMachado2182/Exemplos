import tkinter as tk
from tkinter import ttk



def return_scape(event):
    print('voce epertou a tecla "ESC"')

root = tk.Tk()

btn = ttk.Button(root, text='ESC')
btn.bind('<Escape>', return_scape)

btn.focus()
btn.pack(expand=True)

root.mainloop()