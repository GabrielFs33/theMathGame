import tkinter as tk 
import time
from tkinter import messagebox
from utilitario import resetTela,rodape,criarBotaoOp,criarCabecalho,criarNumeros
from logicaJogo import DadosFuncionais

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


        self.tempoLabelRef = []
        criarCabecalho(root, partidaAtual, pontuacao, self.pararJogo, self.tempoLabelRef)
        self.tempoLabel = self.tempoLabelRef[0]

        criarNumeros(root, self.n1, self.n2, self.resultado)

        operacoesFrame = tk.Frame(root,bg="#000000")
        operacoesFrame.pack(pady=30)

        operadoresMapeados = {"+":"+", "-":"-","x":"*","÷":"/"}

        for textoBotao, operadorReal in operadoresMapeados.items():
            botao = criarBotaoOp(
            operacoesFrame,
            texto=textoBotao,
            comando=lambda op=operadorReal: self.verificarResposta(op)
            )
            botao.pack(side="left", padx=10)

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
