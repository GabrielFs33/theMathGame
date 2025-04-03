import tkinter as tk
from telaInstrucoes import TelaInstrucoes
#from utilitarios import resetaTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        #resetaTabela(self.root)
        self.root.title("THE MATH GAME")

    def frameTelaInicial(self):
        rodape = tk.Label(
            self.root,  # Mudou de self.janela para self.root
            text="Desenvolvido por Gabriel (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
        self.root.mainloop()  # Mudou de self.janela.mainloop() para self.root.mainloop()
