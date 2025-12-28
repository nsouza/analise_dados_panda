# %%
from turtle import color
import pandas as pd
from sympy import rotations


# %%
dados_vendas = {
    'produto':    ['Camisa', 'Camisa', 'Calça', 'Jaqueta', 'Vestido', 'Meia', 'Calça', 'Camisa', 'Jaqueta'],
    'preco':      [49.90, 49.90, 129.90, 199.90, 89.90, 9.90, 129.90, 49.90, 199.90],
    'quantidade': [10, 5, 7, 3, 4, 20, 2, 6, 1],
    'Mes':        ['jan', 'fev', 'jan', 'fev', 'jan', 'fev', 'jan', 'fev', 'jan'],
}
# %%
df_vendas = pd.DataFrame(dados_vendas)
df_vendas
# %%
#Calculand a receita total
df_vendas['receitas'] = df_vendas['preco'] * df_vendas['quantidade']
df_vendas
# %%
resumo_vendas = df_vendas.groupby('produto')['receitas'].sum().reset_index()
resumo_vendas
# %%
produtos_altas_vendas = resumo_vendas[resumo_vendas['receitas'] > 1000]
produtos_altas_vendas
# %%
import matplotlib.pyplot as plt
# %%
plt.figure(figsize=(8,5))
plt.bar(resumo_vendas['produto'], resumo_vendas['receitas'], color='skyblue')
plt.title('Receitas Total por Produto')
plt.xlabel('Produto')
plt.ylabel('Receitas')
plt.xticks(rotation=45)
# %%
