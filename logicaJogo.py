import tkinter as tk
import time
import random
from tkinter import messagebox
from fimJogo import FinalJogo


class DadosOperacionais:
    @staticmethod
    def iniciaJogo(telaJogoInstancia, root):
        root.startTime = time.time()
        root.pontuacao = 0
        root. acertos = 0
        root.running = True
        root.continuaJogo = tk.BooleanVar()

        cont = 1
        maxPartidas = 20

        

        while cont <= maxPartidas:
            telaJogoInstancia.gameFrame(root, cont, root.pontuacao)
            root.continuaJogo.set(False)
            root.wait_variable(root.continuaJogo)

            if not root.running:
                messagebox.showinfo("Jogo encerrado", "Você saiu do jogo.")
                return

            cont +=1

        if cont > maxPartidas: 
            final = FinalJogo(root, pontuacao=root.pontuacao, acertos=root.acertos,partidas=maxPartidas)
            final.frameFimJogo()

            

    @staticmethod
    def iniciaPartida(count,max):
        return count,max
    
    @staticmethod
    def iniciaTempo():
        h = 0
        m = 0
        s = 0
        return h,m,s
    
    @staticmethod
    def iniciaPontos(score):
        return score
    
class DadosFuncionais:
    @staticmethod
    def gerarNumeros():
        return random.randint(0,9), random.randint(0,9)
    
    @staticmethod
    def selecionaOperador():
        return random.choice(["+","-","/","*"])
    
    @staticmethod
    def calculaResultado(a,b,operador):
        if operador == "+":
            return a+b
        elif operador == "-":
            return a-b
        elif operador == "*":
            return a*b
        elif operador == "/":
            return round(a/ (b if b != 0 else 1 ), 2)