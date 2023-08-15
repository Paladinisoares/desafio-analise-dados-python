import pandas as pd
import matplotlib.pyplot as plt

# Carregue os dados JSON utilizando a biblioteca Pandas.
df = pd.read_json('dados_compras.json')

# Examine as primeiras linhas do conjunto de dados para entender sua estrutura.
print(df.head())

# Verifique a presença de quaisquer valores ausentes nos dados.
print(df.info())

# Identifique a quantidade total de compras realizadas.
total_compras = df.shape[0]

# Calcule a média, o valor mínimo e máximo gasto por compra.
media_valor_compras = df.mean(numeric_only=True)['Valor']
min_valor_compras = df.min(numeric_only=True)['Valor']
max_valor_compras = df.max(numeric_only=True)['Valor']

# Determine o produto mais caro e o produto mais barato.
produto_mais_caro = ''
produto_mais_barato = ''
for row in df.iterrows():
    if dict(row[1])['Valor'] == max_valor_compras:
        produto_mais_caro = dict(row[1])['Nome do Item']
    if dict(row[1])['Valor'] == min_valor_compras:
        produto_mais_barato = dict(row[1])['Nome do Item']

# Analise a distribuição de gênero entre os consumidores.
feminino = df[df['Sexo'] == 'Feminino']
masculino = df[df['Sexo'] == 'Masculino']
feminino_quantidade = len(feminino)
masculino_quantidade = len(masculino)

# Calcule o valor total gasto em compras por gênero.
valor_total_feminino = feminino['Valor'].sum()
valor_total_masculino = masculino['Valor'].sum()

# Utilize gráficos adequados (como histogramas, gráficos de barras, etc.) para ilustrar os insights obtidos. 
valores = [media_valor_compras, min_valor_compras, max_valor_compras]
nomes = ['Média', 'Mínimo', 'Máximo']

plt.bar(nomes, valores, color=['blue', 'green', 'purple'])

plt.xlabel('Estatísticas')
plt.ylabel('Valores')
plt.title('Valores de Média, Mínimo e Máximo')
plt.show()

# Utilize gráficos adequados (como histogramas, gráficos de barras, etc.) para ilustrar os insights obtidos.

generos = ['Masculino', 'Feminino']
quantidades = [masculino_quantidade, feminino_quantidade]

plt.bar(generos, quantidades, color=['blue', 'pink', 'purple', 'gray'])

plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.title('Distribuição de Gênero entre Consumidores')
plt.show()

# Utilize gráficos adequados (como histogramas, gráficos de barras, etc.) para ilustrar os insights obtidos.
generos = ['Masculino', 'Feminino']
valores_gastos = [valor_total_masculino, valor_total_feminino]

plt.pie(valores_gastos, labels=generos, autopct='%1.1f%%', colors=['blue', 'pink', 'purple', 'gray'])

plt.title('Valor Total Gasto em Compras por Gênero')
plt.show()