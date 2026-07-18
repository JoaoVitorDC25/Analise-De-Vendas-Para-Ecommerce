#Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

#Gerar dados fictícios de vendas:
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
    
    #Cria uma lista com os nomes da cidade
    lista_cidades = list(cidades_estados.keys())  
    
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
        data_pedido = data_inicial + timedelta(days= int(1/5), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        
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
        
        print("Geração de dados concluida.\n")
        
        #Cria um DataFrame a partir da lista de dados de vendas
        return pd.DataFrame(lista_dados_vendas)