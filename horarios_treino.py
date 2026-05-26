import pandas as pd


dados = pd.read_csv("academia.csv")

 
media_horas = dados['academia.csv'].mean()

print("-media de horas de treinos-")
print(f"a media de horas de treino dos alunos e de:{media_horas:.1f} horas")

