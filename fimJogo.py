import tkinter as tk 
from utilitario import resetTela,rodape

class FinalJogo:
    def __init__ (self, root, pontuacao=0, acertos=0, partidas = 0):
        self.root = root
        self.pontuacao = pontuacao
        self.acertos = acertos
        self.partidas = partidas

    def frameFimJogo(self):
        resetTela(self.root)
        self.root.running = False
        self.root.title("Fim do The Math Game")

        self.bgImg = tk.PhotoImage(file="imagens/fim.png")
        self.bgLabel = tk.Label(self.root, image=self.bgImg)
        self.bgLabel.place(x=0,y=0,relwidth=1,relheight=1)

        titulo = tk.Label(self.root, text="FIM JOGO!", font=("Arial",24),bg="#000000",fg="#39ff14")
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text=f"Parabéns pela partida!\n"
            f"Você marcou {self.pontuacao} pontos e acertou {self.acertos} de {self.partidas}\nUm resultado IMPRESSIONANTE!",
            font=("Arial",14),
            bg="#000000",
            fg="#39ff14"
        )
        texto.pack(pady=10)

        botaoPLay = tk.Button(
            self.root,
            text="Jogar novamente",
            command=self.abrirInstrucoes,
            font=("Arial",16),
            width=15,
            height=2,
            bg="#000000",
            fg="#39ff14"
        )
        botaoPLay.pack(pady=20)

        botaoSair = tk.Button(
            self.root,
            text="Sair",
            command=self.sairJogo,
            font=("Arial",16),
            width=15,
            height=2,
            bg="#000000",
            fg="#39ff14"
        )
        botaoSair.pack(pady=10)

        rodape(self.root)

    def abrirInstrucoes(self):
        from telaInstrucoes import TelaInstrucoes
        TelaInstrucoes(self.root).frameTelaInstrucoes()

    def sairJogo(self):
        self.root.running = False
        self.root.destroy()

