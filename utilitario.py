import tkinter as tk
def resetTela(root):
    for widget in root.winfo_children():
        widget.destroy()

def rodape(root):
    rodape = tk.Label(
        root,
        text="Desenvolvido por:\nGabriel Firmiano e Hugo Miguel (Senai Betim 2025)",
        font=("Arial", 12),
        bg="#000000",
        fg="#39ff14"
    )
    rodape.pack(side="bottom", pady=10)
    return rodape

def criarBotaoOp(root, texto, comando):
    return tk.Button(
        root,
        text=texto,
        fg="#39ff14",
        bg="#000000",
        activebackground="#000000",
        activeforeground="#39ff14",
        font=("Arial", 16),
        width=5,
        height=3,
        highlightthickness=0,
        command=comando
    )

def criarCabecalho(root, partidaAtual, pontuacao, pararCallback, tempoLabelRef):
    cabecalho = tk.Frame(root, bg="#000000")
    cabecalho.pack(pady=10)

    tk.Label(cabecalho, text="Partida:", fg="#39ff14", bg="#000000").grid(row=0, column=0, padx=10)
    tk.Label(cabecalho, text=f"{partidaAtual}/20", fg="#39ff14", bg="#000000").grid(row=0, column=1, padx=10)

    tk.Label(cabecalho, text="Pontuação:", fg="#39ff14", bg="#000000").grid(row=0, column=2, padx=10)
    tk.Label(cabecalho, text=str(pontuacao), fg="#39ff14", bg="#000000").grid(row=0, column=3, padx=10)

    tk.Label(cabecalho, text="", fg="#39ff14", bg="#000000").grid(row=0, column=4, padx=10)

    tempoLabel = tk.Label(cabecalho, text="", fg="#39ff14", bg="#000000")
    tempoLabel.grid(row=0, column=5, padx=10)
    tempoLabelRef.append(tempoLabel)

    botaoParar = tk.Button(cabecalho, text="Pausar", fg="#39ff14", bg="#000000", font=("Arial", 10), command=pararCallback)
    botaoParar.grid(row=0, column=6, padx=10)

    return cabecalho

def criarNumeros(root,n1,n2,resultado):
    numerosFrame = tk.Frame(root,bg="#000000")
    numerosFrame.pack(pady=40)

    tk.Label(numerosFrame, text=str(n1), fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=20)
    tk.Label(numerosFrame, text="👽", fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=20)
    tk.Label(numerosFrame, text=str(n2), fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=20)
    tk.Label(numerosFrame, text="=", fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=10)
    tk.Label(numerosFrame, text=str(resultado), fg="#39ff14", bg="#000000", font=("Arial", 32)).pack(side="left", padx=10)

    return numerosFrame