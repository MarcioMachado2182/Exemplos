#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        tk2 = tk.Tk(master)
        tk2.configure(
            background="#ed5854",
            height=200,
            highlightbackground="#eb56e8",
            highlightcolor="#efe852",
            width=200)
        tk2.geometry("640x480")
        tk2.title("Janela")
        label3 = ttk.Label(tk2)
        label3.configure(
            background="#7ae75a",
            foreground="#373700",
            text='Isto é uma Label')
        label3.pack(
            anchor="center",
            expand=False,
            fill="both",
            ipadx=50,
            ipady=50,
            padx=0,
            pady=0,
            side="top")
        button2 = ttk.Button(tk2)
        button2.configure(text='Isto é um Botão')
        button2.pack(
            anchor="center",
            expand=False,
            padx=50,
            pady=10,
            side="top")
        text1 = tk.Text(tk2)
        text1.configure(
            background="#43efef",
            font="{Algerian} 16 {italic}",
            foreground="#c76bb7",
            height=10,
            width=50)
        text1.pack(side="top")

        # Main widget
        self.mainwindow = tk2

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
