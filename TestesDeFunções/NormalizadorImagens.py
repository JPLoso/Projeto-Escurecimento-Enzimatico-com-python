from PIL import Image
import cv2
import numpy as np
# Caminho da imagem (pode ser PNG, JPG, etc.)
entrada = "/home/joao-pedro-veloso/Documentos/ProjetoEngenhariaAlimentos/TestesDeFunções/ChatGPT Image 24 de set. de 2025, 20_00_53.png"
saida = "imagem_convertida.png"

# 1. Abre com Pillow
img_pil = Image.open(entrada)

# 2. Converte para RGB (remove transparência e garante 8 bits)
img_pil = img_pil.convert("RGB")

# 3. Salva em formato seguro
img_pil.save(saida)

# 4. Lê com OpenCV
img_cv2 = cv2.imread(saida, cv2.IMREAD_COLOR)

# Verificação
if img_cv2 is None:
    print("Erro ao carregar imagem")
else:
    print("Imagem carregada com sucesso:", img_cv2.shape)

    # Exibe
    cv2.imshow("Imagem convertida", img_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()