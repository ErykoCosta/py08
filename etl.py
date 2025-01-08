import pandas as pd
import os

# Caminho da pasta onde os arquivos JSON estão localizados
data_folder = 'data'

# Lista de arquivos JSON a serem lidos
json_files = ['coleta_dia01.json', 'coleta_dia02.json', 'coleta_dia03.json']

def read_concat (data_folder, json_files):
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
    else:
        print("Nenhum arquivo foi carregado para concatenar.")

    # Salvar o DataFrame concatenado em um arquivo CSV (opcional)
    # output_file = 'data/combined_data.csv'
    # combined_df.to_csv(output_file, index=False)
    # print(f"\nDataFrame concatenado salvo como '{output_file}'.")


