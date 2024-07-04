import tkinter as tk

# Configuração da janela principal
menu_inicial = tk.Tk()
menu_inicial.geometry("400x400")
menu_inicial.title("Grid Layout with Borders")

# Frame
frame = tk.Frame(menu_inicial, borderwidth=2, relief="solid")
frame.pack( fill="both")

# Adicionar labels no frame
label1 = tk.Label(frame, text="label1", font="Arial 20", bg="red")
label1.grid(row=0, column=0)

label2 = tk.Label(frame, text="label2", font="Arial 20", bg="green")
label2.grid(row=0, column=1)



# Executar a aplicação
menu_inicial.mainloop()