#Bibliotecas
import pandas as pd
import seaborn as sns
import config as cfg

import data_generator as dg
import utils as ut
import charts as ch

from matplotlib.ticker import FuncFormatter

ut.clear()
ch.configurar_estilo()
    
#Gerar os dados de vendas
df_vendas = dg.gerar_dados_vendas(cfg.NUMERO_DE_REGISTROS)

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

# ========== Top 10 Produtos mais vendidos ==========
# Dados
top10_vendas = df_vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
ut.text("Top 10 Produtos mais vendidos (quantidade total):\n", top10_vendas)

# Gráfico
ch.grafico_barras_horizontal(
    dados=top10_vendas.sort_values(ascending=True),
    titulo="Top 10 Produtos mais vendidos (quantidade total)",
    xlabel="Quantidade total vendida",
    ylabel="Produto",
    cor="skyblue",
    caminho= "images/top10_produtos_mais_vendidos.png")

# ========== Faturamento mensal ==========
# Dados
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')
ut.text("Faturamento Mensal:\n", faturamento_mensal)

# Gráfico
ch.grafico_linha(
    dados=faturamento_mensal,
    titulo="Evolução do Faturamento Mensal",
    xlabel="Mês",
    ylabel="Faturamento (R$)",
    cor="green",
    marker="o",
    linestyle="-",
    caminho= "images/faturamento_mensal.png")

# ========== Faturamento por estado ==========
# Dados
faturamento_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)
ut.text("Faturamento por Estado:\n", faturamento_estado)

# Gráfico
ch.grafico_barras_vertical(
    dados=faturamento_estado,
    titulo="Faturamento por Estado",
    xlabel="Estado",
    ylabel="Faturamento (R$)",
    cor=sns.color_palette("husl", 7),
    caminho= "images/faturamento_por_estado.png")

# ========== Faturamento por categoria ==========
# Dados
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)
ut.text("Faturamento por Categoria:\n", faturamento_categoria)
faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

def formatador_milhares(y, pos):
    """Formata o valor em milhares (K) com o cifrão R$."""
    return f'R$ {y/1000:,.0f}K'

formatter = FuncFormatter(formatador_milhares)

# Gráfico
ch.grafico_barras_vertical(
    dados=faturamento_categoria,
    titulo="Faturamento por Categoria",
    xlabel="Categoria",
    ylabel="Faturamento",
    cor=sns.color_palette("viridis", len(faturamento_categoria)),
    rotacao_x=45,
    formatter=formatter,
    caminho= "images/faturamento_por_categoria.png")