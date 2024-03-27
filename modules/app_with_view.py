import tkinter as tk
import json
import locale
from tkinter import ttk
from modules.app import App
from modules.produto import Produto

# Define a formatação para o Real brasileiro (BRL)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class AppWithView(App):
    def __init__(self, root):
        super().__init__(root)

        # Botão para visualizar produtos
        self.visualizar_produtos_button = tk.Button(self.root, text="Visualizar Produtos", command=self.visualizar_produtos)
        self.visualizar_produtos_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Carrega os produtos do arquivo
        self.carregar_produtos()

    def carregar_produtos(self):
        try:
            with open("produtos.json", "r") as file:
                produtos_data = json.load(file)
                self.produtos = [Produto(**produto) for produto in produtos_data]
        except FileNotFoundError:
            self.produtos = []

    def salvar_produtos(self):
        with open("produtos.json", "w") as file:
            produtos_data = [produto.__dict__ for produto in self.produtos]
            json.dump(produtos_data, file)

    def cadastrar_produto(self):
        super().cadastrar_produto()
        self.salvar_produtos()

    def visualizar_produtos(self):
        # Cria uma nova janela para exibir os produtos
        self.produtos_window = tk.Toplevel(self.root)
        self.produtos_window.title("Produtos Cadastrados")
        
        # Frame para exibir os produtos
        produtos_frame = tk.Frame(self.produtos_window)
        produtos_frame.pack(padx=20, pady=20)
        
        # Cabeçalho da listagem
        tk.Label(produtos_frame, text="Nome").grid(row=0, column=0)
        tk.Label(produtos_frame, text="Descrição").grid(row=0, column=1)
        tk.Label(produtos_frame, text="Valor").grid(row=0, column=2)
        tk.Label(produtos_frame, text="Disponível para Venda").grid(row=0, column=3)
        
        # Exibe os produtos na nova janela
        for i, produto in enumerate(self.produtos, start=1):
            tk.Label(produtos_frame, text=produto.nome).grid(row=i, column=0)
            tk.Label(produtos_frame, text=produto.descricao).grid(row=i, column=1)
            tk.Label(produtos_frame, text=locale.currency(produto.valor, grouping=True)).grid(row=i, column=2)
            tk.Label(produtos_frame, text="Sim" if produto.disponivel_para_venda else "Não").grid(row=i, column=3)