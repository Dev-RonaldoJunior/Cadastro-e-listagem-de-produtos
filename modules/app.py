import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from modules.produto import Produto

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro e Listagem de Produtos")
        
        self.produtos = []
        
        # Frame para o formulário de cadastro
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=20, pady=20)
        
        tk.Label(self.form_frame, text="Nome do produto:").grid(row=0, column=0, sticky="w")
        self.nome_entry = tk.Entry(self.form_frame)
        self.nome_entry.grid(row=0, column=1)
        
        tk.Label(self.form_frame, text="Descrição do produto:").grid(row=1, column=0, sticky="w")
        self.descricao_entry = tk.Entry(self.form_frame)
        self.descricao_entry.grid(row=1, column=1)
        
        tk.Label(self.form_frame, text="Valor do produto:").grid(row=2, column=0, sticky="w")
        self.valor_entry = tk.Entry(self.form_frame)
        self.valor_entry.grid(row=2, column=1)
        
        tk.Label(self.form_frame, text="Disponível para venda:").grid(row=3, column=0, sticky="w")
        self.disponivel_combobox = ttk.Combobox(self.form_frame, values=["Sim", "Não"])
        self.disponivel_combobox.grid(row=3, column=1)
        
        # Botão para cadastrar produto
        self.cadastrar_button = tk.Button(self.form_frame, text="Cadastrar", command=self.cadastrar_produto)
        self.cadastrar_button.grid(row=4, columnspan=2, pady=10)
        
        # Frame para a listagem de produtos
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(padx=20, pady=20)
        
        # # Cabeçalho da listagem
        # tk.Label(self.list_frame, text="Nome").grid(row=0, column=0)
        # tk.Label(self.list_frame, text="Valor").grid(row=0, column=1)
        
        # Botão para abrir o formulário de cadastro
        self.novo_produto_button = tk.Button(self.list_frame, text="Novo Produto", command=self.abrir_formulario)
        self.novo_produto_button.grid(row=0, column=2)
        
    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        descricao = self.descricao_entry.get()
        valor = float(self.valor_entry.get())
        disponivel_para_venda = self.disponivel_combobox.get()
        
        if disponivel_para_venda == "Sim":
            disponivel_para_venda = True
        else:
            disponivel_para_venda = False
        
        produto = Produto(nome, descricao, valor, disponivel_para_venda)
        self.produtos.append(produto)
        
    def listar_produtos(self):
        # Limpa a listagem atual
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        # Ordena os produtos por valor
        self.produtos.sort(key=lambda x: x.valor)
        
        # Exibe os produtos na listagem
        for i, produto in enumerate(self.produtos, start=1):
            tk.Label(self.list_frame, text=produto.nome).grid(row=i, column=0)
            tk.Label(self.list_frame, text=str(produto.valor)).grid(row=i, column=1)
        
    def abrir_formulario(self):
        self.nome_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.disponivel_combobox.set("Sim")
        self.form_frame.lift()