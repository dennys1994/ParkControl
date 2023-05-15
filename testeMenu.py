import tkinter as tk
from tkinter import ttk
import datetime
import sqlite3
import makeBd

class MenuScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.menu_label = tk.Label(self, text="Selecione a tela:")
        self.menu_label.pack()

        self.tela1_button = tk.Button(self, text="Cadastrar Veiculo", command=self.show_tela1)
        self.tela1_button.pack()

        self.tela2_button = tk.Button(self, text="Consultar Veiculos", command=self.show_tela2)
        self.tela2_button.pack()

    def show_tela1(self):
        self.destroy()
        Tela1Screen(self.master)

    def show_tela2(self):
        self.destroy()
        Tela2Screen(self.master)

class Tela1Screen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tela_label = tk.Label(self, text="Cadastrar Veiculo")
        self.tela_label.grid(row=0, column=0, columnspan=2)

        def update_label():
            makeBd.cadastrarVeiculo(tipoVeiculo.get(),placa.get(),telefone.get())
            resultado.config(text="Veiculo cadastrado com sucesso!")
            placa.delete(0,tk.END)
            telefone.delete(0,tk.END)
            tipoVeiculo.set(options[0])

        #opcoes de veiculo
        options = ["Moto", "Carro pequeno", "Carro grande"]
        tipoVeiculo = tk.StringVar(self)
        tipoVeiculo.set(options[0])

        labelVeiculo = tk.Label(self, text="Tipo Veiculo: ")
        labelVeiculo.grid(row=1, column=0, sticky="W")

        dropdown = tk.OptionMenu(self, tipoVeiculo, *options)
        dropdown.grid(row=1, column=1, sticky="E")

        #caixa de texto para placa e telefone
        labelPlaca = tk.Label(self, text="Placa: ")
        labelPlaca.grid(row=2, column=0, sticky="W")

        placa = tk.Entry(self)
        placa.grid(row=2, column=1, sticky="E")

        labelPhone = tk.Label(self, text="Telefone: ")
        labelPhone.grid(row=3, column=0, sticky="W")

        telefone = tk.Entry(self)
        telefone.grid(row=3, column=1, sticky="E")

        resultado = tk.Label(self, text="")
        resultado.grid(row=4, column=0, columnspan=2)

        inserirVeiculo = tk.Button(self, text="Cadastrar!", command=update_label)
        inserirVeiculo.grid(row=5, column=0, columnspan=2)  

        self.voltar_button = tk.Button(self, text="Voltar", command=self.show_menu)
        self.voltar_button.grid(row=6, column=0, columnspan=2)

    def show_menu(self):
        self.destroy()
        MenuScreen(self.master)



class Tela0Screen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tela_label = tk.Label(self, text="Cadastrar Veiculo")
        self.tela_label.pack()

        def update_label():
            makeBd.cadastrarVeiculo(tipoVeiculo.get(),placa.get(),telefone.get())
            resultado.config(text="Veiculo cadastrado com sucesso!")
            placa.delete(0,tk.END)
            telefone.delete(0,tk.END)
            tipoVeiculo.set(options[0])

        #opcoes de veiculo
        options = ["Moto", "Carro pequeno", "Carro grande"]
        tipoVeiculo = tk.StringVar(self)
        tipoVeiculo.set(options[0])

        dropdown = tk.OptionMenu(self, tipoVeiculo, *options)
        dropdown.pack()

        #caixa de texto para placa e telefone
        labelPlaca = tk.Label(self, text="Placa: ")
        labelPlaca.pack()

        placa = tk.Entry(self)
        placa.pack()

        labelPhone = tk.Label(self, text="Telefone: ")
        labelPhone.pack()

        telefone = tk.Entry(self)
        telefone.pack()

        resultado = tk.Label(self, text="")
        resultado.pack()  

        inserirVeiculo = tk.Button(self, text="Cadastrar!", command=update_label)
        inserirVeiculo.pack()    

        self.voltar_button = tk.Button(self, text="Voltar", command=self.show_menu)
        self.voltar_button.pack()

    def show_menu(self):
        self.destroy()
        MenuScreen(self.master)

class Tela2Screen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tela_label = tk.Label(self, text="Consultar Veiculos")
        self.tela_label.grid(row=0, column=0, columnspan=2)

        # Cria um novo frame para colocar os widgets da tabela
        table_frame = tk.Frame(self)
        table_frame.grid(row=1, column=0, columnspan=2)

        # Cria uma scrollbar para a tabela
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Cria uma tabela para mostrar os dados da tabela
        treeview = ttk.Treeview(table_frame, yscrollcommand=scrollbar.set)
        treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define as colunas da tabela
        treeview["columns"] = ("Tipo", "Placa", "Data", "Hora Chegada", "Telefone")

        # Define o cabeçalho da tabela
        treeview.heading("Tipo", text="Tipo")
        treeview.heading("Placa", text="Placa")
        treeview.heading("Data", text="Data")
        treeview.heading("Hora Chegada", text="Hora Chegada")
        treeview.heading("Telefone", text="Telefone")

        # Define as larguras das colunas
        treeview.column("Tipo", width=100)
        treeview.column("Placa", width=100)
        treeview.column("Data", width=100)
        treeview.column("Hora Chegada", width=100)
        treeview.column("Telefone", width=100)

        # Cria uma conexão com o banco de dados
        conn = sqlite3.connect('estacionamento.db')

        # Executa a instrução SQL para selecionar todos os veículos na tabela
        cursor = conn.execute("SELECT * FROM veiculos")

        # Adiciona as informações de cada veículo à tabela
        for row in cursor:
            treeview.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        
        # Fecha a conexão com o banco de dados
        conn.close()

        scrollbar.config(command=treeview.yview)

        self.voltar_button = tk.Button(self, text="Voltar", command=self.show_menu)
        self.voltar_button.grid(row=2, column=1)

    def show_menu(self):
        self.destroy()
        MenuScreen(self.master)


#iniciador grafico
root = tk.Tk()
root.geometry("800x600+0+0")
app = MenuScreen(master=root)
app.mainloop()
