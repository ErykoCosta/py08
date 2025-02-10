import pandas as pd
import os

# Caminho da pasta onde os arquivos JSON estão localizados
data_folder = 'data'

# Lista de arquivos JSON a serem lidos
json_files = ['coleta_dia01.json', 'coleta_dia02.json', 'coleta_dia03.json']

def read_concat(data_folder, json_files):
    # Lista para armazenar os DataFrames
    dataframes = []
    
    # Loop para ler e concatenar os arquivos JSON
    for file in json_files:
        file_path = os.path.join(data_folder, file)
        try:
            # Lê o arquivo JSON e adiciona à lista
            df = pd.read_json(file_path)
            dataframes.append(df)
            print(f"Arquivo '{file}' lido com sucesso!")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{file}': {e}")
    
    # Concatenar todos os DataFrames em um único DataFrame
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        print("\nDataFrame concatenado:")
        print(combined_df)
        
        # Adicionando a coluna "Total" ao DataFrame combinado
        if "quantidade" in combined_df.columns and "Venda" in combined_df.columns:
            combined_df["Total"] = combined_df["Quantidade"] * combined_df["Venda"]
            print("\nDataFrame com a coluna 'Total' adicionada:")
            print(combined_df)
        else:
            print("\nColunas 'quantidade' ou 'Venda' não encontradas no DataFrame.")
        
        # Retorna o DataFrame final para uso posterior, se necessário
        return combined_df
    else:
        print("Nenhum arquivo foi carregado para concatenar.")
        return None

# Executa a função
df_final = read_concat(data_folder, json_files)

# Se quiser salvar o DataFrame final em um arquivo CSV (opcional)
if df_final is not None:
    df_final.to_csv("resultado_final.csv", index=False)
    print("\nDataFrame final salvo como 'resultado_final.csv'.")