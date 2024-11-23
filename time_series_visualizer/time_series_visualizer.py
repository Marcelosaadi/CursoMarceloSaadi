import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
dados_limpos = dados[(dados['value'] >= dados['value'].quantile(0.025)) & 
                     (dados['value'] <= dados['value'].quantile(0.975))]

def plotar_grafico_linha():
    figura, eixo = plt.subplots(figsize=(12, 6))
    eixo.plot(dados_limpos.index, dados_limpos['value'], color='red', linewidth=1)
    eixo.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    eixo.set_xlabel("Date")
    eixo.set_ylabel("Page Views")
    plt.tight_layout()
    figura.savefig('line_plot.png')
    return figura

def plotar_grafico_barra():
    dados_barra = dados_limpos.copy()
    dados_barra['ano'] = dados_barra.index.year
    dados_barra['mes'] = dados_barra.index.month
    dados_agrupados = dados_barra.groupby(['ano', 'mes'])['value'].mean().unstack()

    figura_barra = dados_agrupados.plot(kind='bar', figsize=(12, 8), legend=True).figure
    plt.title('Monthly Average Page Views per Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.tight_layout()
    figura_barra.savefig('bar_plot.png')
    return figura_barra

def plotar_grafico_box():
    dados_boxplot = dados_limpos.copy()
    dados_boxplot['ano'] = dados_boxplot.index.year
    dados_boxplot['mes'] = dados_boxplot.index.strftime('%b')
    dados_boxplot['mes_num'] = dados_boxplot.index.month
    dados_boxplot = dados_boxplot.sort_values('mes_num')

    figura_box, eixos = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(ax=eixos[0], x='ano', y='value', data=dados_boxplot)
    eixos[0].set_title('Year-wise Box Plot (Trend)')
    eixos[0].set_xlabel('Year')
    eixos[0].set_ylabel('Page Views')

    sns.boxplot(ax=eixos[1], x='mes', y='value', data=dados_boxplot)
    eixos[1].set_title('Month-wise Box Plot (Seasonality)')
    eixos[1].set_xlabel('Month')
    eixos[1].set_ylabel('Page Views')
    plt.tight_layout()
    figura_box.savefig('box_plot.png')
    return figura_box
