import random
from tkinter import messagebox
#from fimJogo import FinalJogo

class DadosOperacionais:
    @staticmethod
    def iniciaJogo(telaJogoInstancia, root):
        cont = 1
        maxPartidas = 20
        root.pontuacao = 0

        while cont <= maxPartidas:
            telaJogoInstancia.gameFrame(root, cont, root.pontuacao)#em caso de erro trocar para frameTelaJogo '-'
            root.continuaJogo.set(False)
            root.wait_variable(root.continuaJogo)

            if not root.running:
                messagebox.showinfo("Jogo encerrado", "Você saiu do jogo.")
                break

            cont +=1

            if cont > maxPartidas:
                messagebox.showinfo("Fim do jogo",f"Parabéns! Você marcou {root.pontuacao} pontos no jogo.")

   
        
    @staticmethod
    def iniciaPartida(count,max):
        return count,max
    
    @staticmethod
    def iniciaTempo():
        m=00
        s=00
        h=00
        return m,s,h
    
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