import pandas as pd
import os
os.system('cls')
data = {
    'Produto': ['Camisa', 'Calça', 'Jaqueta', 'Tênis', 'Mochila'],
    'Categoria': ['Vestuário', 'Vestuário', 'Vestuário', 'Calçados', 'Acessórios'],
    'Preço': [50, 120, 250, 200, 100],
    'Quantidade': [30, 15, 8, 12, 20]
}

df = pd.DataFrame(data)

#Criando nova coluna, filtrando e fazendo a média.
df['Valor total'] = df['Preço'] * df['Quantidade']
filtro = df[df['Preço'] < 150]
media = df['Preço'].mean()

print('Menor que 150 \n', filtro)
print('Media dos preços: \n', media)
