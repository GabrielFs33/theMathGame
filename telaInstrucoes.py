import tkinter as tk
from utilitario import resetTela

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
            text = "Clique no botão correspondente a resposta",
            font=("Arial",14)
        )
        instrucoes.pack(pady=10)

 
        btJogar = tk.Button(
            self.root,
            text="Começar",
            font=("Arial", 16),
            width=12,
            height=2,
            
        )
        btJogar.pack(pady=30)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por Gabriel (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

