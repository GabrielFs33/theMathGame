import tkinter as tk 
from utilitario import resetTela
from logicaJogo import DadosOperacionais,DadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.operadorCorreto = None
        self.n1 = None
        self.n2 = None
        self.result = None

    def gameFrame(self, root, partidaAtual, pontuacao):
        resetTela(self.root)
        self.root.title("The Math GAME")

        
        self.n1, self.n2 = DadosFuncionais.gerarNumeros()
        self.operadorCorreto = DadosFuncionais.selecionaOperador()
        self.resultado = DadosFuncionais.calculaResultado(self.n1, self.n2, self.operadorCorreto)
        self.pontuacao = pontuacao
       

        cabecalho = tk.Frame(root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{partidaAtual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(pontuacao)).grid(row=0, column=3, padx=10)

        botaoParar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=self.pararJogo)
        botaoParar.grid(row=0, column=6, padx=10)
        '''
        tk.Label(cabecalho, text="Tempo:").grid(row=0, column=4, padx=10)
        tk.Label(cabecalho, text="0").grid(row=0, column=5, padx=10)
        '''

        numerosFrame = tk.Frame(root)
        numerosFrame.pack(pady=40)

        tk.Label(numerosFrame, text=str(self.n1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text=str(self.n2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numerosFrame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numerosFrame, text=str(self.resultado), font=("Arial", 32)).pack(side="left", padx=10)

        operacoesFrame = tk.Frame(root)
        operacoesFrame.pack(pady=30)

        operadoresMapeados = {"+":"+", "-":"-","x":"*","÷":"/"}

        for textoBotao, operadorReal  in operadoresMapeados.items():
            botao = tk.Button(
                operacoesFrame,
                text=textoBotao,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda op=operadorReal: self.verificarResposta(op)
            ).pack(side="left", padx=10)

        rodape = tk.Label(
            root,
            text="Desenvilvido por: \nGabriel Firmianono e Hugo Miguel (Senai Betim 2025)",
            font=("Arial",8)
        )
        rodape.pack(side="bottom",padx=10)

    def verificarResposta(self, resposta):
        if resposta == self.operadorCorreto:
            print("Acertou!")
            self.root.pontuacao += 199
        else:
            print("Errou!")
        

        self.root.continuaJogo.set(True)


    def pararJogo(self):
        self.root.destroy()
        self.root.running = False
        self.root.continuaJogo.set(True)
