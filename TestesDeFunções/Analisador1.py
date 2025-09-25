import cv2
import numpy as np
import Normalizador_Imagens as NI

# Carregar imagem
img = cv2.imread("/home/joao-pedro-veloso/Documentos/ProjetoEngenhariaAlimentos/TestesDeFunções/ChatGPT Image 24 de set. de 2025, 20_00_53.png")
if img is None:
    print("Erro ao carregar a imagem")
    exit()

# Normalizar imagem
img = NI.NormalizadorImagens(img)

# Reduzir para metade do tamanho
altura = img.shape[0] // 2
largura = img.shape[1] // 2
imgr = cv2.resize(img, (largura, altura))
print("Nova forma:", imgr.shape)

# Criar máscara (preto próximo de 0)
mask = cv2.inRange(imgr, (0,0,0), (40,40,40))

# Mostrar máscara
cv2.imshow("Mascara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
