import tkinter as tk

janela = tk.Tk()
janela.title("Olá mundo com Tkinter")
janela.geometry("400x300")

lblMsg = tk.Label(janela, text="Olá Mundo!", font=("Arial", 24))
lblMsg.pack()

janela.mainloop()
