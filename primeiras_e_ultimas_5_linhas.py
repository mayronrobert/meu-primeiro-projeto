import pandas as pd

# Arquivo identificado na sua barra lateral
ARQUIVO_ACADEMIA = "academia.csv"

try:
    # Carrega os dados da sua academia
    dados = pd.read_csv(ARQUIVO_ACADEMIA)

    # 1. Exibe as primeiras 5 linhas
    print("\n--- PRIMEIRAS 5 LINHAS ---")
    print(dados.head(5))

    # 2. Exibe as últimas 5 linhas
    print("\n--- ÚLTIMAS 5 LINHAS ---")
    print(dados.tail(5))

    # 3. Exibe o total de linhas e colunas
    print("\n--- DIMENSÕES DA TABELA ---")
    print(f"Total de Linhas: {dados.shape[0]}")
    print(f"Total de Colunas: {dados.shape[1]}")
    print(f"Formato (linhas, colunas): {dados.shape}\n")

except FileNotFoundError:
    print(f"\n❌ Erro: O arquivo '{ARQUIVO_ACADEMIA}' não foi localizado na pasta atual.")
except Exception as e:
    print(f"\n❌ Ocorreu um erro ao ler o arquivo: {e}")

