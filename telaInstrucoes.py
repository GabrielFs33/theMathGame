import tkinter as tk
from utilitario import resetTela
from telaJogo import TelaJogo
from logicaJogo import DadosOperacionais

class TelaInstrucoes:
    def __init__(self,root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetTela(self.root)
        self.root.title("Instruções do jogo")

        titulo = tk.Label(
            self.root,
            text="Instruções do jogo",
            font=("Arial",20)
        )
        titulo.pack(pady=20)

        instrucoes = tk.Label(
            self.root,
            text = "Clique no operador correspondente ao resultado da operação entre os números \n {+} {-} {/} {*}",
            font=("Arial",14)
        )
        instrucoes.pack(pady=10)


        btJogar = tk.Button(
            self.root,
            text="Começar",
            font=("Arial", 16),
            width=12,
            height=2,
            command=self.irPraJogo
        )
        btJogar.pack(pady=30)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por Gabriel Firmiano  e Hugo Miguel (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def irPraJogo(self):
        telaJogo = TelaJogo(self.root)
        DadosOperacionais.iniciaJogo(telaJogo,self.root)

