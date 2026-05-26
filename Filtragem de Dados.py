import pandas as pd  

dados = pd.read_csv("academia.csv") 

treinam_muito = dados[dados['Horas_Treino'] > 5]

print("alunos que treinam mais de 5 horas por semana")
print(treinam_muito)