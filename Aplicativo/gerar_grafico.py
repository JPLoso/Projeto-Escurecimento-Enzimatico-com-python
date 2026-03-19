import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from calc_percentual import calc_percentuais

def carregar_imagem(caminho):
    img_pil = Image.open(caminho).convert("RGB")
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def criar_mascara(img):
    mask_no_black = cv2.inRange(img, (40,40,40), (255,255,255))

    contornos, _ = cv2.findContours(mask_no_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:3]

    mask_final = np.zeros(img.shape[:2], dtype="uint8")

    if len(contornos) == 0:
        return mask_no_black

    for cnt in contornos:
        cv2.drawContours(mask_final, [cnt], -1, 255, -1)

    return mask_final

def analisar_imagem(img, mask):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return calc_percentuais(mask, gray)

def plotar_grafico(valores):
    categorias = ["Escuras", "Médias", "Claras"]

    plt.figure(figsize=(6,4))
    plt.bar(categorias, valores)

    for i, v in enumerate(valores):
        plt.text(i, v+1, f"{v:.1f}%", ha='center')

    plt.ylim(0,100)
    plt.title("Distribuição de claridade")
    plt.ylabel("% dos Pixels")
    plt.show()

def gerar_grafico(caminho):
    img = carregar_imagem(caminho)
    mask = criar_mascara(img)
    valores = analisar_imagem(img, mask)
    plotar_grafico(valores)

    return valores