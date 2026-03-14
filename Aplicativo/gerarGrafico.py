import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from calc_percentual import calc_percentuais

def gerarGrafico(entrada):
    saida = "imagem_convertida.png"
    img_pil = Image.open(entrada).convert("RGB")
    img_pil.save(saida)
    img = cv2.imread(saida)

    if img is None:
        print("Erro ao carregar")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ✅ Criar máscara para ignorar fundo preto
    mask_no_black = cv2.inRange(img, (40,40,40), (255,255,255))

    # ✅ Detectar objetos apenas para delimitar onde analisar
    contornos, _ = cv2.findContours(mask_no_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:3]  # até 3 objetos

    # ✅ Máscara final só com pixels que fazem parte dos objetos (sem fundo)
    mask_final = np.zeros(gray.shape, dtype="uint8")

    # Se não encontrar contornos, analisa imagem inteira exceto preto
    if len(contornos) == 0:
        mask_final = mask_no_black
    else:
        for cnt in contornos:
            cv2.drawContours(mask_final, [cnt], -1, 255, -1)

    # ✅ Calcular percentual total (um único resultado)
    valores = calc_percentuais(mask_final, gray)

    categorias = ["Escuras", "Médias", "Claras"]

    plt.figure(figsize=(6,4))
    plt.bar(categorias, valores)
    for i, v in enumerate(valores):
        plt.text(i, v+1, f"{v:.1f}%", ha='center')

    plt.ylim(0,100)
    plt.title("Distribuição de claridade)")
    plt.ylabel("% dos Pixels")
    plt.show()
