import tkinter as tk
from telaInstrucoes import TelaInstrucoes
from utilitario import resetTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        resetTela(self.root)
        self.root.title("THE MATH GAME")

    def frameTelaInicial(self):
        titulo = tk.Label(self.root, text="Bem-vindo ao \nTHE MATH GAME!", font=("Arial", 14))
        titulo.pack(pady=50)

        btPlay = tk.Button(
            self.root,
            text="Play",
            font=("Arial", 20),
            width=10,
            height=2
        )
        btPlay.pack(pady=20)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por Gabriel (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.root.mainloop()
