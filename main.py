import tkinter as tk
from modules.app import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.listar_produtos()  # Mostra a listagem inicial de produtos ao iniciar o programa
    root.mainloop()