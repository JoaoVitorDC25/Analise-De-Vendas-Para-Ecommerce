import matplotlib.pyplot as plt
import seaborn as sns
import config as cfg

def configurar_estilo():
    """
    Configura o estilo padrão dos gráficos.
    """
    sns.set_style("darkgrid")
    
def grafico_barras_horizontal(
        dados,
        titulo,
        xlabel,
        ylabel,
        cor="skyblue",
        figsize=cfg.FIGURA_PADRAO
    ):

    plt.figure(figsize=figsize)

    dados.plot(
        kind="barh",
        color=cor
    )

    plt.title(titulo, fontsize=cfg.FONTSIZE_TITLE)
    plt.xlabel(xlabel, fontsize=cfg.FONTSIZE_LABELS)
    plt.ylabel(ylabel, fontsize=cfg.FONTSIZE_LABELS)

    plt.tight_layout()
    plt.show()

def grafico_linha(
        dados,
        titulo,
        xlabel,
        ylabel,
        cor="green",
        marker="o",
        linestyle="-",
        figsize=cfg.FIGURA_PADRAO
    ):

    plt.figure(figsize=figsize)

    dados.plot(
        kind="line",
        marker=marker,
        linestyle=linestyle,
        color=cor
    )

    plt.title(titulo, fontsize=cfg.FONTSIZE_TITLE)
    plt.xlabel(xlabel, fontsize=cfg.FONTSIZE_LABELS)
    plt.ylabel(ylabel, fontsize=cfg.FONTSIZE_LABELS)

    plt.tight_layout()
    plt.show()
    
def grafico_barras_vertical(
    dados,
    titulo,
    xlabel,
    ylabel,
    cor=None,
    figsize=cfg.FIGURA_PADRAO,
    rotacao_x=0,
    formatter=None
    ):

    if cor is None:
        cor = sns.color_palette("viridis", len(dados))

    fig, ax = plt.subplots(figsize=figsize)

    dados.plot(
        kind="bar",
        ax=ax,
        color=cor
    )

    ax.set_title(titulo, fontsize=cfg.FONTSIZE_TITLE)
    ax.set_xlabel(xlabel, fontsize=cfg.FONTSIZE_LABELS)
    ax.set_ylabel(ylabel, fontsize=cfg.FONTSIZE_LABELS)

    if formatter:
        ax.yaxis.set_major_formatter(formatter)

    plt.xticks(rotation=rotacao_x)

    plt.tight_layout()
    plt.show()