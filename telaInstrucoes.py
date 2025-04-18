import tkinter as tk
from utilitario import resetTela,rodape
from telaJogo import TelaJogo
from logicaJogo import DadosOperacionais

class TelaInstrucoes:
    def __init__(self,root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetTela(self.root)
        self.root.title("Instruções do jogo")
        self.root.configure(bg="#000000")

        titulo = tk.Label(
            self.root,
            text="Instruções do jogo",
            font=("Arial",20),
            bg="#000000",
            fg="#39ff14"
        )
        titulo.pack(pady=20)

        instrucoes = tk.Label(
            self.root,
            text = "Clique no operador que melhor substitui o 👽 ",
            font=("Arial",18),
            bg="#000000",
            fg="#39ff14"
        )
        instrucoes.pack(pady=10)

        operadores = tk.Label(
            self.root,
            text = "+  -  /  *",
            font=("Arial",18),
            bg="#000000",
            fg="#ffff99"
        )
        operadores.pack(pady=10)

        btJogar = tk.Button(
            self.root,
            text="Começar",
            font=("Arial", 16),
            width=12,
            height=2,
            bg="#000000",
            fg="#39ff14",
            command=self.irPraJogo
        )
        btJogar.pack(pady=30)

        rodape(self.root)

    def irPraJogo(self):
        telaJogo = TelaJogo(self.root)
        DadosOperacionais.iniciaJogo(telaJogo,self.root)

