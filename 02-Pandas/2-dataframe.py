# %%
import pandas as pd

# %%
dados = {
    'nome': ['Alice', 'Bob', 'Charlie'],
    'idade': [24,30,22],
    'cidade': ['São Paulo','Rio de janeiro', 'Belo Horizonte']
}

# %%
df = pd.DataFrame(dados)
df
# %%
df.head(1)

# %%
df.tail(1)
# %%

# ...existing code...
# %%
# exemplo no formato que você mostrou (listas alinhadas por índice)
dados_notas = {
    'nome': ['Carlos', 'Gabi', 'Alice', 'Bruno', 'Diego'],
    'Matematica': [5, 9, 8, 6, 7],
    'Portugues':  [7, 8, 9, 5, 6],
    'Historia':   [6, 7, 8, 6, 9],
}

df_notas = pd.DataFrame(dados_notas)
print(df_notas)

# %%
# ou gerando notas aleatórias (0.0 - 10.0, 1 casa decimal)
import random

nomes = ['Carlos', 'Gabi', 'Alice', 'Bruno', 'Diego']
materias = ['Matematica', 'Portugues', 'Historia']

dados_notas = {'nome': nomes}
for m in materias:
    dados_notas[m] = [round(random.uniform(0, 10), 1) for _ in nomes]

df_notas = pd.DataFrame(dados_notas)

# ...existing code...
# %%
#Calcular media de notas por Aluno
df_notas['Média'] = df_notas[['Matematica','Portugues','Historia']].mean(1)
df_notas

# %%
#alunos aprovado com nota boa (média >= 8)
alunos_aprovados = df_notas[df_notas['Média'] >= 6]
alunos_aprovados
# %%
#Exibit apenas alunos aprovado
alunos_aprovados[['nome','Média']]


# %%
