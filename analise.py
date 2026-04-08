import pandas as pd

# carregar dados
df = pd.read_csv('razao_mortalidade_materna.csv', sep=';', skiprows=2)
import os

print(os.listdir())

# renomear colunas (IMPORTANTE)
df.columns = ['Local', 'Ano', 'Variavel', 'Valor']

# ver dados
print(df.head())

# 🔹 FILTRAR só o que importa
df = df[df['Variavel'].str.contains('Razão de mortalidade materna', na=False)]

# 🔹 limpar valores
df['Valor'] = df['Valor'].astype(str)
df['Valor'] = df['Valor'].str.replace(',', '.')
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

# remover nulos
df = df.dropna()

# 🔹 ver resultado limpo
print("\nDados tratados:")
print(df.head())

# 📊 análise por ano
por_ano = df.groupby('Ano')['Valor'].mean()
print("\nMédia por ano:")
print(por_ano)

# 📊 estatísticas
print("\nEstatísticas:")
print(df['Valor'].describe())

import matplotlib.pyplot as plt

por_ano.plot()
plt.title("Evolução da Mortalidade Materna no Brasil")
plt.xlabel("Ano")
plt.ylabel("Razão de mortalidade")
plt.show()