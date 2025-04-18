import tkinter as tk
from telaInstrucoes import TelaInstrucoes
from utilitario import resetTela,rodape
class TelaInicial:
    def __init__(self, root):
        self.root = root
        resetTela(self.root)
        self.root.title("THE MATH GAME")

    def frameTelaInicial(self):
        

        self.bgImg = tk.PhotoImage(file="imagens/fundoTelaAbertura.png")
        self.bgLabel = tk.Label(self.root, image=self.bgImg)
        self.bgLabel.place(x=0,y=0,relwidth=1,relheight=1)

        self.imgPlay = tk.PhotoImage(file="imagens/alienzin.png")
        self.imgPlay = self.imgPlay.subsample(4, 4)
        
        btPlay = tk.Button(
            self.root,
            image=self.imgPlay,
            borderwidth=0,
            highlightthickness=0,
            command=self.irParaInstrucoes
        )
        btPlay.place(relx=0.5,rely=0.7,anchor="center")
        
        labelInstrucao = tk.Label(
            self.root,
            text="Clique no alien para começar",
            font=("Arial", 14, "bold"),
            bg="#000000",   
            fg="#39ff14"    
        )
        labelInstrucao.place(relx=0.5, rely=0.5, anchor="s")


        rodape(self.root)
        
    def irParaInstrucoes(self):
            TelaInstrucoes(self.root).frameTelaInstrucoes()

