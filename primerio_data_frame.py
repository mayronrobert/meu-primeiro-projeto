import pandas as pd

dados_frutas = {
    "Fruta": ["Maçã", "Banana", "Morango", "Uva", "Abacaxi"],
    "Quantidade": [15,24, 18, 15, 78],
    "Preco": [4.50, 3.00, 7.50, 6.00, 5.00]
}

df_frutas = pd.DataFrame(dados_frutas)

print("--- DATAFRAME DE FRUTAS ---")
print(df_frutas)

