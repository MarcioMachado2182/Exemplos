#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

def opcao(event):
    tecla = event.char
    match tecla:
        case "1":
            label1.config(text="Você escolheu: Ala Minuta")           
        case '2':
            label1.config(text="Você escolheu: Lazanha")
        case "3":
            label1.config(text="Você escolheu: Strogonofe")
        case "4":
            label1.config(text="Você escolheu: Tilapia")

# build ui
tk1 = tk.Tk()
tk1.geometry("800x600")
tk1.title("minha gui")
label1 = ttk.Label(tk1)
label1.configure(
    anchor="center",
    background="#0080ff",
    cursor="arrow",
    font="{Arial Baltic} 20 {}",
    foreground="#ffff00",
    text='Escolha uma opção:\n (1) Ala Minuta\n (2) Lazanha\n (3) Strogonofe\n (4) Tilapia' )
label1.pack(expand=True, fill="x", side="top")

tk1.bind("<Key-1>",opcao)
tk1.bind("<Key-2>",opcao)
tk1.bind("<Key-3>",opcao)
tk1.bind("<Key-4>",opcao)

tk1.mainloop()