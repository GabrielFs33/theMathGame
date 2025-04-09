import tkinter as tk 
from utilitario import resetTela
class TelaJogo:
    def __init__(self, root):
        self.root = root

    def gameFrame(self,root,partida,pontuacao):
        resetTela(self.root)

        self.root.title("The Math GAME")

        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0,column=0,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=1, padx=10),

        tk.Label(cabecalho, text="Partida:").grid(row=0,column=2,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=3,padx=10)

        tk.Label(cabecalho, text="Tempo:").grid(row=0,column=4,padx=10)
        tk.Label(cabecalho, text="0").grid(row=0,column=5,padx=10)

        botaoParar = tk.Button(cabecalho, text="Parar", font=("Arial",10), command=lambda: self.pararJogo(self))
        botaoParar.grid(row=0,column=6,padx=10)

        numerosFrame= tk.Frame(self.root)
        numerosFrame.pack(pady=40)

        tk.Label(numerosFrame, text="1", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text="?", font=("Arial", 32)).pack(side="left", padx=20)

        tk.Label(numerosFrame, text="2", font=("Arial",32)).pack(side="left",padx=20)
        tk.Label(numerosFrame, text="=", font=("Arial", 32)).pack(side="left",padx=20)

        tk.Label(numerosFrame, text="3",font=("Arial",32)).pack(side="left",padx=20)

        operacoesFrame= tk.Frame(self.root)
        operacoesFrame.pack(pady=30)

        for operacao in ["+","-","/","*"]:
            tk.Button(operacoesFrame, text=operacao, font=("Arial",16), width=5, height=2).pack(side="left",padx=10)

    def pararJogo(self,root):
        self.root.destroy()