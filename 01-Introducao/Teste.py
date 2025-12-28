# %%
print('a')

# %%
import pandas as pd
df1 = pd.DataFrame({'nome':['Nilo','Nilda'],'idade':[51,52]})

df2 = pd.DataFrame({'bairro':['Bairu','Santa Cruz'],'Cidade':['juiz de fora','São João Nepomuceno']})

resultado = pd.concat([df1,df2], ignore_index= True)
print(resultado)
# %%
