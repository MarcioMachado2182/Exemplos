import tkinter as tk

# Configuração da janela principal
rosto = tk.Tk()
rosto.geometry("400x400")
rosto.title("Rosto Canvas")

canvas = tk.Canvas(rosto, width=400, height=400, bg='green')
canvas.pack(anchor=tk.CENTER, expand=True)

canvas.create_rectangle(100,100,180,160, fill='black', outline='black')#Olho esquerdo
canvas.create_rectangle(240,100,320,160, fill='black', outline='black')#Olho direito
canvas.create_rectangle(180,160,240,260, fill='black', outline='black')#nariz
canvas.create_rectangle(150,220,190,310, fill='black', outline='black')#Boca lado esquerdo
canvas.create_rectangle(240,220,280,310, fill='black', outline='black')#Boca lado direito



rosto.mainloop()