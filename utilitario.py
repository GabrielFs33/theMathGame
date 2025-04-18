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