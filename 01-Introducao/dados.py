# %%

from networkx import dfs_edges
import pandas as pd

# %%
data = {
    'produto': ['camiseta','calça', 'Tênis'],
    'Quantidade': [20,15,10],
    'Preço Unitário': [50.0, 70.0, 120.0]
}

df = pd.DataFrame(data)

# %%
df
# %%
df['Total'] = df['Quantidade'] * df['Preço Unitário']
df


# %%
df_pedidos = pd.read_csv("data/Pedidos.csv",sep=",")
df_pedidos

# %%
df_pedidos['Total'] = df_pedidos['Unidades'] * df_pedidos['PrecoUnidade']
df_pedidos

# %%
df_pedidos.head(10)
# %%
df_pedidos.tail(5)

# %%
vendas_por_regiao = df_pedidos.groupby('Regiao')['Total'].sum().reset_index()
vendas_por_regiao
# %%
