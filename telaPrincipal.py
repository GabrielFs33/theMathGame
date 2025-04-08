import tkinter as tk
from tkinter import messagebox
from telaAbertura import TelaInicial
from telaInstrucoes import TelaInstrucoes

def frameGenerico():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("The Math Game")
    root.resizable(False, False)

    root.continue_game = tk.BooleanVar(value=False)
    root.running = True

    def funcaoFechar():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            root.running = False
            root.continue_game.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", funcaoFechar)

    return root


'''
window = buildMain()
excluir dps
try:
    window.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")
'''

#execução principal
if __name__ == "__main__":
    root = frameGenerico()
    telaAbertura = TelaInicial(root)
    telaAbertura.frameTelaInicial()

    try:
        root.mainloop()
    except Exception as e:
        print(f"Erro durante a execução: {e}")
