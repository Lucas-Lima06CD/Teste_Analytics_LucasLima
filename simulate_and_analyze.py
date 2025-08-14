# Case realizado via Google collab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd

# Criando Data Set
rom datetime import datetime, timedelta

# Gerando datas aleatórias (intervalo de jan a dez 2023)
def gerar_data_aleatoria(n):

# Criando um df apartir de 1 de janeiro de 2023 até 31 de dezembro
 start_date = datetime(2023, 1, 1)
 end_date = datetime(2023, 12, 31)

# Lista de criação dos dados
 return[start_date + timedelta(days=rd.randint(0, 364))for _ in range(n)]

# Gerando Produtos e Categorias

Produtos = [
('Banana','Frutas'),
('Maçã','Frutas'),
('Laranja','Frutas'),
('Abobora', 'Legumes'),
('Batata', 'Legumes'),
('Cenoura','Legumes'),
('Alface','Folhas'),
('Agrião','Folhas')
]

n = 60

# Criando o DataFrame

DF = pd.DataFrame({
    'ID': range(1, n+1),
    'Data': gerar_data_aleatoria(n),
    'Produto':[rd.choice(Produtos)[0]for _ in range(n)],
    'Categoria':[rd.choice(Produtos)[1]for _ in range(n)],
    'Quantidade' :np.random.randint(1, 10, size=n),
    'Preço' :np.random.uniform(50, 5000, size=n).round(2)
})

# Inserindo dados com erros propositalmente (NAN e Duplicatas)

DF.loc[5, 'Preço'] = np.nan
DF.loc[10, 'Produto'] = np.nan
DF = pd.concat([DF, DF.iloc[0]], ignore_index=True)

# Analisando número de produtos
DF['Categoria'].value_counts()

# Remoção de Valores NAN
DF['Produto'].fillna('Produto desconhecido', inplace = True)
DF['Preço'].fillna(DF['Preço'].mean(), inplace = True)
DF['Categoria'].fillna('Categoria desconhecida', inplace = True)

# Verificando se ainda restam valores NAN
DF['Produto'].isnull().sum()

# Removendo Duplicatas
DF.drop_duplicates(inplace = True)

# Garantindo a integridade dos Dados

DF['Data'] = pd.to_datetime(DF['Data']) # Ordena que esse tipo de dado seja data
DF['Quantidade'] = DF['Quantidade'].fillna(0).astype(int)
DF['Preço'] = DF['Preço'].astype(float)

# Criando uma nova coluna e multiplicando a quantidade pelo preço
DF['Total_vendas'] = DF['Quantidade'] * DF['Preço']
# Total de vendas da multiplicação
Total_vendas = DF.groupby('Produto')['Total_vendas'].sum().sort_values(ascending=False)

# Produto mais vendido
produto_mais_vendido = Total_vendas.idxmax()

from google.colab import files

DF.to_csv('DF.csv', index=False)
files.download('DF.csv')

# Tendencias de Vendas Mensais ao longo do tempo
DF['Mês'] = DF['Data'].dt.month
Vendas_por_mes = DF.groupby('Mês')['Quantidade'].sum()
Vendas_por_mes = Vendas_por_mes.reset_index()

# Plot do Gráfico

plt.figure(figsize=(15,7))
plt.plot(Vendas_por_mes['Mês'], Vendas_por_mes['Quantidade'], marker='o', linestyle='-', color ='green')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.grid(True)
plt.show()

# 1. O mês 2 apresentou o menor número de vendas em comparação aos outros meses
# 2. Os meses 6 e 9 foram os meses com os melhores resultados de vendas.
# 3. Após o mês 10 é esperado um equilíbrio médio nas vendas

from google.colab import files

DF.to_csv('DF.csv', index=False)
files.download('DF.csv')