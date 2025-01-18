import pandas as pd
import os
os.system('cls')

#adicionar pizzas ao pedido com nome, quantidade e preço uni
df = pd.DataFrame(columns=['Nome', 'Preco_uni', 'Quantidade', 'Total'])

def adicionar_pizzas(nome, preco_uni, quantidade):
    global df
    novo_produto = {
        'Nome': nome, 'Preco_uni': preco_uni, 'Quantidade': quantidade, 'Total': preco_uni * quantidade
    }
    df = df._append(novo_produto, ignore_index=True)

adicionar_pizzas('Muzzarela', 55, 2)

#Exibir uma lista de todos os itens adicionados
print(df)