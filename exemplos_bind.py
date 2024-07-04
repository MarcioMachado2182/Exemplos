import tkinter as tk
from tkinter import ttk
def apertei():
    print('apertei.')

def return_pressed(event):
    print('Return key pressed.')


root = tk.Tk()

btn = ttk.Button(root, text='Save',command=apertei)
btn.bind('<Return>', return_pressed)


btn.focus()#precisa do focus para manter o botão em foco e ler o bind() dele
btn.pack(expand=True)

root.mainloop()

