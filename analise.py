"""
Projeto: Análise de Eficiência e Geração de Energia
Descrição: Script desenvolvido para processar logs de geração de sistemas fotovoltaicos,
calculando a eficiência diária e identificando desvios em relação à capacidade nominal.
Autor(a): Daniella Santos
"""

import pandas as pd


def analisar_dados_geracao(caminho_csv):
  """Carrega os dados de geração de energia, trata valores ausentes

  e calcula a taxa de eficiência operacional do sistema.
  """
  print("Carregando histórico de dados de geração...")

  # Tratamento de exceção para garantir estabilidade caso o arquivo falhe
  try:
    df = pd.read_csv(caminho_csv)

    # Verificando se as colunas necessárias existem
    colunas_necessarias = [
        "Data",
        "Irradiancia",
        "Energia_Gerada_kWh",
        "Capacidade_Nominal",
    ]
    for col in colunas_necessarias:
      if col not in df.columns:
        raise ValueError(f"A coluna '{col}' está ausente no arquivo de dados.")

    # Limpeza de dados: preenchendo eventuais nulos com 0
    df["Energia_Gerada_kWh"] = df["Energia_Gerada_kWh"].fillna(0)

    # Cálculo da eficiência percentual (Gerada vs Nominal)
    df["Eficiencia_Percentual"] = (
        df["Energia_Gerada_kWh"] / df["Capacidade_Nominal"]
    ) * 100

    print("Processamento e cálculos concluídos com sucesso.")
    return df

  except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_csv}' não foi localizado.")
    return None
  except Exception as e:
    print(f"Erro inesperado durante o processamento: {e}")
    return None


if __name__ == "__main__":
  # Simulação de execução com um arquivo de log anterior
  arquivo_historico = "historico_geracao_solar.csv"
  resultado_analise = analisar_dados_geracao(arquivo_historico)

  if resultado_analise is not None:
    print("\nResumo dos dados processados:")
    print(resultado_analise.head())
  else:
    print("A execução foi interrompida por falha nos dados.")
