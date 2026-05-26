import pandas as pd

dados = pd.read_csv("academia.csv")

print("-3 primeiras linhas-")
print (dados.head(3))

print("\n-nomes das colunas-")
print(dados.columns)