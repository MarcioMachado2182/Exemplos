import tkinter as tk
from tkinter import ttk


def salvar():
    print('enviado')    

def return_pressed(event):
    print('enviado')


root = tk.Tk()

btn = ttk.Button(root, text='Save',command=salvar)
btn.bind('<Return>', return_pressed)#testem qualquer tecla


btn.focus()
btn.pack(expand=True)

root.mainloop()
