import tkinter as tk


janela = tk.Tk()
janela.geometry("400x400")
janela.title("Carinha Sorrindo")

def criando(x, y, color, f_color):
    label1 = tk.Label(janela, text=str, bg=color, fg=f_color, width=2, height=2)
    label1.place(x=x, y=y)

criando(50, 50, "blue", "green") #Olho esquerdo 
criando(350, 50, "blue", "green") #2 Olho direito
criando(200, 150, "blue", "green") #2 Olho direito


criando(200, 300, "blue", "green") #2 Centro da boca
criando(230, 300, "blue", "green") 
criando(170, 300, "blue", "green")  
criando(260, 300, "blue", "green") 
criando(140, 300, "blue", "green") 
criando(290, 280, "blue", "green") 
criando(320, 250, "blue", "green") 
criando(110, 280, "blue", "green") 
criando(80, 250, "blue", "green") 


janela.mainloop()





