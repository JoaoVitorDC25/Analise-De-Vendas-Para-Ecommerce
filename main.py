#Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

import config as cfg
import utils as ut

from datetime import datetime, timedelta

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

ut.clear()

#Gerar dados fictícios de vendas, default 600 registros:
def gerar_dados_vendas(num_registros=600):
    
    """
    Gera um DataFrame com dados fictícios de vendas.
    """
    
    print(f"Iniciada a geração de {num_registros} registros de vendas...")
    
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }
    
    # Cria listas para armazenar os dados
    lista_produtos = list(produtos.keys())
    
    #Aarmazena os dados em listas
    lista_dados_vendas = []
      
    #Dicionario com cidades e estados brasileiros
    cidades_estados = {
        'São Paulo': 'SP',
        'Rio de Janeiro': 'RJ',
        'Belo Horizonte': 'MG',
        'Curitiba': 'PR',
        'Porto Alegre': 'RS',
        'Salvador': 'BA',
        'Fortaleza': 'CE',
        'Recife': 'PE',
        'Brasília': 'DF',
        'Manaus': 'AM'
    }
    
    #Cria uma lista com os nomes da cidade
    lista_cidades = list(cidades_estados.keys())  
    
    data_inicial = datetime(2026, 1, 1)
    
    #Gerar registros de vendas
    for _ in range(num_registros):
        
        #Seleciona um produto aleatório da lista de produtos
        produto = random.choice(lista_produtos)
        
        #Seleciona uma cidade aleatória da lista de cidades
        cidade = random.choice(lista_cidades)
        
        #Gera uma quantidade aleatória entre 1 e 7
        quantidade = random.randint(1, 7)
        
        #Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days= int(_/5), hours=random.randint(0, 23))
        
        #Se o produto for mouse ou teclado, desconto de 10%
        if produto in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto]['preco'] * 0.9
        else:
            preco_unitario = produtos[produto]['preco'] 
            
        #Adicionar um registro de venda à lista
        lista_dados_vendas.append({
            'Produto': produto,
            'Categoria': produtos[produto]['categoria'],
            'Cidade': cidade,
            'Estado': cidades_estados[cidade],
            'Quantidade': quantidade,
            'Preco_Unitario': preco_unitario,
            'Data_Pedido': data_pedido
        })  
            
    #Cria um DataFrame a partir da lista de dados de vendas
    print("Geração de dados concluida.\n")    
    return pd.DataFrame(lista_dados_vendas)
    
#Gerar os dados de vendas
df_vendas = gerar_dados_vendas(cfg.NUMERO_DE_REGISTROS)

#Shape (número de linhas e colunas) do DataFrame
ut.text("Shape do DataFrame (linhas, colunas):",df_vendas.shape)

#Exibe informações sobre o DataFrame, como tipos de dados e valores nulos
ut.text("Informações sobre o DataFrame:")
df_vendas.info()

#Resumo estatistico do DataFrame, incluindo contagem, média, desvio padrão, valores mínimo e máximo
ut.text("Resumo estatístico do DataFrame:\n",df_vendas.describe())

df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

#Engenharia de atributos:
#Cria a coluna faturamento, que é o resultado da multiplicação da quantidade pelo preço unitário
df_vendas['Faturamento'] = df_vendas['Quantidade'] * df_vendas['Preco_Unitario']
#Coluna de status de entrega:
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda Estado: 'Rápida' if Estado in ['SP', 'RJ', 'MG'] else 'Normal')

ut.text(f"Exibindo as {cfg.AMOSTRAS} primeiras linhas do DataFrame:\n",
        df_vendas[['Produto','Data_Pedido','Estado','Status_Entrega']].head(cfg.AMOSTRAS))

ut.text(f"Exibindo as {cfg.AMOSTRAS} últimas linhas do DataFrame:\n",
        df_vendas[['Produto','Data_Pedido','Estado','Status_Entrega']].tail(cfg.AMOSTRAS))

#Top 10 Produtos mais vendidos, ordenados pela quantidade total vendida
top10_vendas = df_vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
ut.text("Top 10 Produtos mais vendidos (quantidade total):\n", top10_vendas)

#Gráfico
sns.set_style("whitegrid")
plt.figure(figsize=(12, 7))

top10_vendas.sort_values(ascending=True).plot(kind='barh', color='skyblue')

plt.title("Top 10 Produtos mais vendidos (quantidade total)", fontsize=16)
plt.xlabel("Quantidade total vendida", fontsize=12)
plt.ylabel("Produto", fontsize=12)

#Exibe o gráfico
plt.tight_layout()
plt.show()

#Faturamento mensal
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

#Converte o faturamento
#faturamento_mensal = faturamento_mensal.map('R$ {:,.2f}'.format)

#Grafico de faturamento mensal
plt.figure(figsize=(12, 6))

faturamento_mensal.plot(kind='line', marker='o',linestyle='-', color='green')

plt.title("Evolução do Faturamento Mensal", fontsize=16)
plt.xlabel("Mês", fontsize=12)
plt.ylabel("Faturamento (R$)", fontsize=12)

plt.xticks(rotation=45)
#Exibe o gráfico
plt.tight_layout()
plt.show()

