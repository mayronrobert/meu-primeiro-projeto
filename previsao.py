


import matplotlib.pyplot as plt


dados = {
    'Minutos': [10, 20, 30, 40, 50],
    'Calorias': [100, 200, 300, 400, 500]
}


df = pd.Dataframe(dados)


print("Tabela de Progressão Linear:")


previsao_60_min = 60 * 10


print(f"\nPrevisão: Em 60 minutos, você queimará {previsao_60_min} calorias.")
