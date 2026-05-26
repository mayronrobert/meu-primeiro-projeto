
import sqlite3


conexao = sqlite3.connect('meu_projeto_dados.db')


cursor = conexao.cursor()


comando_ddl = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
);
"""


cursor.execute(comando_ddl)
print("Estrutura do banco de dados criada com sucesso usando DDL!")
print("-" * 50)


print("--- CADASTRO DE NOVO CLIENTE ---")
nome_usuario = input("Digite o nome do cliente: ")
idade_usuario = int(input("Digite a idade do cliente: "))



cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?);", (nome_usuario, idade_usuario))


conexao.commit()
print("-" * 50)
print(f"Sucesso! O cliente '{nome_usuario}' foi cadastrado no banco de dados.")


cursor.close()
conexao.close()
print("Conexão com o banco de dados encerrada com segurança.")
