import pandas as pd

dados = pd.read_csv("academia.csv")


contagem_idades = dados["Idade"].value_counts()

print("--- Contagem de alunos por idade ---")
print(contagem_idades)

