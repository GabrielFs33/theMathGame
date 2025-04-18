import tkinter as tk 
import time
from tkinter import messagebox
from utilitario import resetTela,rodape
from logicaJogo import DadosOperacionais,DadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.tempoPausado = 0
        self.tempoAntersDaPausa = 0
        self.root = root
        self.operadorCorreto = None
        self.n1 = None
        self.n2 = None
        self.result = None

        self.tempoLabel = None
        self.timerId = None
        self.pause = None

        self.iniciaTempo = 0    

    def gameFrame(self, root, partidaAtual, pontuacao):
        resetTela(self.root)
        self.root.title("The Math GAME")

        self.iniciaTempo = time.time()
        self.root.startTime = time.time()

        self.bg_image = tk.PhotoImage(file="imagens/alienBgGame.png")  
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        self.n1, self.n2 = DadosFuncionais.gerarNumeros()
        self.operadorCorreto = DadosFuncionais.selecionaOperador()
        self.resultado = DadosFuncionais.calculaResultado(self.n1, self.n2, self.operadorCorreto)
        self.pontuacao = pontuacao


        cabecalho = tk.Frame(root,bg="#000000")
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:", fg="#39ff14", bg="#000000").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{partidaAtual}/20",fg="#39ff14", bg="#000000",).grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:", fg="#39ff14", bg="#000000").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(pontuacao),fg="#39ff14", bg="#000000").grid(row=0, column=3, padx=10)
        
        botaoParar = tk.Button(cabecalho, text="Pausar", fg="#39ff14", bg="#000000", font=("Arial", 10), command=self.pararJogo)
        botaoParar.grid(row=0, column=6, padx=10)
        
        tk.Label(cabecalho, text="",fg="#39ff14", bg="#000000").grid(row=0, column=4, padx=10)
        self.tempoLabel = tk.Label(cabecalho,text="",fg="#39ff14", bg="#000000")
        self.tempoLabel.grid(row=0, column=5, padx=10)
        

        numerosFrame = tk.Frame(root,bg="#000000")
        numerosFrame.pack(pady=40)

        tk.Label(numerosFrame, text=str(self.n1),fg="#39ff14", bg="#000000",font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text="👽",fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text=str(self.n2),fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text="=",fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numerosFrame, text=str(self.resultado), fg="#39ff14", bg="#000000",font=("Arial", 32)).pack(side="left", padx=10)

        operacoesFrame = tk.Frame(root,bg="#000000")
        operacoesFrame.pack(pady=30)

        operadoresMapeados = {"+":"+", "-":"-","x":"*","÷":"/"}

        for textoBotao, operadorReal  in operadoresMapeados.items():
            botao = tk.Button(
                operacoesFrame,
                text=textoBotao,
                fg="#39ff14", 
                bg="#000000",
                font=("Arial", 16),
                width=5,
                height=3,
                command=lambda op=operadorReal: self.verificarResposta(op)
            ).pack(side="left", padx=10)

        self.paused = False
        self.atualizarTempo()

        rodape(self.root)

    def verificarResposta(self, resposta):

        if resposta == self.operadorCorreto:
            tempoDecorridoQuestao = time.time() - self.iniciaTempo
            if tempoDecorridoQuestao < 20:
                self.root.pontuacao += 10*199
            else:
                self.root.pontuacao += 199
            self.root.acertos += 1
            print("Acertou")
        else:
            print("Errou!")
        

        self.root.continuaJogo.set(True)

    def atualizarTempo(self):
        if not self.root.running or self.paused:
            return
        elapsed = int(time.time() -self.root.startTime)
        minutos = elapsed // 60
        segundos = elapsed %60
        self.tempoLabel.config(text=f"Tempo: {minutos:02d}:{segundos:02d}")
        self.timerId = self.root.after(1000, self.atualizarTempo)



    def pararJogo(self):
        self.paused = True
        self.tempoAntersDaPausa = time.time() - self.root.startTime
        if messagebox.askyesno("Em pausa", "Deseja voltar para a tela inicial?"):
            from telaAbertura import TelaInicial
            TelaInicial(self.root).frameTelaInicial()
        else:
            self.paused = False
            self.root.startTime = time.time() - self.tempoAntersDaPausa
            self.atualizarTempo()
