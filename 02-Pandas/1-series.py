# %%
import pandas as pd


# %%
dados = [10,20,30,40,50]
serie = pd.Series(dados)
serie

# %%
# listar métodos públicos
[m for m in dir(serie) if not m.startswith('_')]

# ver docstring de um método específico
print(serie.mean.__doc__)

# ou usar help()
help(pd.Series)        # classe
help(serie.mean)       # métodom
# %%
