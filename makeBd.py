import datetime
import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('estacionamento.db')

# Cria uma tabela "veiculos" no banco de dados
conn.execute('''CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    placa TEXT NOT NULL,
    data_chegada TEXT NOT NULL,
    hora_chegada TEXT NOT NULL,
    telefone TEXT NOT NULL
);''')

# Fecha a conexão com o banco de dados
conn.close()

def cadastrarVeiculo(tipo, placa, telefone):
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('estacionamento.db')

    # Obtém a data e hora atual
    agora = datetime.datetime.now()

    # Formata a data e hora como uma string no formato "YYYY-MM-DD HH:MM:SS"
    data_chegada = agora.strftime("%Y-%m-%d")
    hora_chegada = agora.strftime("%H:%M:%S")

     # Insere o novo veículo na tabela "veiculos"
    conn.execute("INSERT INTO veiculos (tipo, placa, data_chegada, hora_chegada, telefone) VALUES (?, ?, ?, ?, ?)", (tipo, placa, data_chegada, hora_chegada, telefone))

    # Confirma a inserção dos dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

def imprimirVeiculos():
    # Cria uma conexão com o banco de dados
    conn = sqlite3.connect('estacionamento.db')

    # Executa a instrução SQL para selecionar todos os veículos na tabela
    cursor = conn.execute("SELECT * FROM veiculos")

    # Itera sobre os resultados e imprime as informações de cada veículo
    for row in cursor:
        print(f"Tipo: {row[1]} Placa: {row[2]}  Data: {row[3]}\n")
        print(f"Horário de Chegada: {row[4]} Telefone: {row[5]}\n\n")

    # Fecha a conexão com o banco de dados
    conn.close()