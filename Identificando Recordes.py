import pandas as pd

dados = pd.read_csv("academia.csv")


maior_idade = dados['Idade'].max()
menor_idade = dados['Idade'].min()

print("recorde de idade na academia")
print(f"O aluno mais velho tem: {maior_idade} anos.")
print(f"O aluno mais novo tem: {menor_idade} anos.")
