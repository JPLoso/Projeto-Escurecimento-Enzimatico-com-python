#Importações de funções internas
from plotar_grafico import plotar_grafico
from analisar_imagem import analisar_imagem
from criar_mascara import criar_mascara
from carregar_imagem import carregar_imagem

#Define a função para gerar grafico
def gerar_grafico(caminho):
    img = carregar_imagem(caminho)
    mask = criar_mascara(img)
    valores = analisar_imagem(img, mask)
    plotar_grafico(valores)

    return valores