import tkinter as tk


janela = tk.Tk()
janela.geometry("400x400")
janela.title("Janela com nomes")

frame = tk.Frame(janela, borderwidth=1)
frame.pack(fill = "both")


def create_label(frame, text, row, column):
    label = tk.Label(frame , text=text,relief= "solid", borderwidth=2, bg = "silver")
    label.grid(row=row, column=column, sticky="nsew")

  
create_label(frame, "MARCIO", 0, 0)
create_label(frame, "LUCAS", 0, 1)
create_label(frame, "SARAH", 1, 0)
create_label(frame, "FELIPE", 1, 1)

for i in range(2):
    frame.grid_columnconfigure(i, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)


janela.mainloop()

