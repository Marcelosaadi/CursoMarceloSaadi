import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: Import the data
df_dados = pd.read_csv('medical_examination.csv')

# 2: Add 'overweight' column
df_dados['acima_peso'] = (df_dados['weight'] / ((df_dados['height'] / 100) ** 2) > 25).astype(int)

# 3: Normalize cholesterol and gluc values
df_dados['colesterol'] = (df_dados['cholesterol'] > 1).astype(int)
df_dados['glicose'] = (df_dados['gluc'] > 1).astype(int)

# 4: Define the draw_cat_plot function
def desenhar_cat_plot():
    # 5: Create DataFrame for cat plot using pd.melt
    df_catplot = pd.melt(df_dados, id_vars=['cardio'], 
                         value_vars=['colesterol', 'glicose', 'smoke', 'alco', 'active', 'acima_peso'])

    # 6: Group and reformat the data
    df_catplot = df_catplot.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7: Create the catplot
    figura_cat = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                             data=df_catplot, kind='bar', height=5, aspect=1).fig

    # 8: Save the plot
    figura_cat.savefig('catplot.png')
    return figura_cat

# 10: Define the draw_heat_map function
def desenhar_mapa_calor():
    # 11: Clean the data
    df_calor = df_dados[(df_dados['ap_lo'] <= df_dados['ap_hi']) &
                        (df_dados['height'] >= df_dados['height'].quantile(0.025)) &
                        (df_dados['height'] <= df_dados['height'].quantile(0.975)) &
                        (df_dados['weight'] >= df_dados['weight'].quantile(0.025)) &
                        (df_dados['weight'] <= df_dados['weight'].quantile(0.975))]

    # 12: Calculate the correlation matrix
    matriz_correlacao = df_calor.corr()

    # 13: Generate a mask for the upper triangle
    mascara = np.triu(np.ones_like(matriz_correlacao, dtype=bool))

    # 14: Set up the matplotlib figure
    figura_matriz, eixo = plt.subplots(figsize=(10, 10))

    # 15: Draw the heatmap
    sns.heatmap(matriz_correlacao, mask=mascara, annot=True, fmt=".1f", square=True, cbar_kws={'shrink': 0.5}, ax=eixo)

    # 16: Save the plot
    figura_matriz.savefig('heatmap.png')
    return figura_matriz
