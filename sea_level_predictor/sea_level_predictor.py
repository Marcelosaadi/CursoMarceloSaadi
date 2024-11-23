import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def gerar_grafico():
    dados_nivel_mar = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(dados_nivel_mar['Year'], dados_nivel_mar['CSIRO Adjusted Sea Level'], label="Original Data", color="blue")

    inclinacao, intercepto, _, _, _ = linregress(dados_nivel_mar['Year'], dados_nivel_mar['CSIRO Adjusted Sea Level'])
    anos_estendidos = pd.Series(range(1880, 2051))
    linha_geral = inclinacao * anos_estendidos + intercepto
    plt.plot(anos_estendidos, linha_geral, label="Best Fit: 1880-2050", color="green")

    dados_recente = dados_nivel_mar[dados_nivel_mar['Year'] >= 2000]
    inclinacao_recente, intercepto_recente, _, _, _ = linregress(dados_recente['Year'], dados_recente['CSIRO Adjusted Sea Level'])
    anos_recente = pd.Series(range(2000, 2051))
    linha_recente = inclinacao_recente * anos_recente + intercepto_recente
    plt.plot(anos_recente, linha_recente, label="Best Fit: 2000-2050", color="red")

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()
