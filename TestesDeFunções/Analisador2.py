import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Caminho da imagem
entrada = "/home/joao-pedro-veloso/Documentos/ProjetoEngenhariaAlimentos/TestesDeFunções/ChatGPT Image 24 de set. de 2025, 20_00_53.png"
saida = "imagem_convertida.png"

# 1. Converter imagem para RGB usando Pillow (garante formato limpo)
img_pil = Image.open(entrada).convert("RGB")
img_pil.save(saida)

# 2. Ler imagem com OpenCV (BGR)
img = cv2.imread(saida)
if img is None:
    print("Erro ao carregar imagem")
    exit()

# 3. Reduz tamanho para acelerar processamento (opcional)
altura = img.shape[0] // 2
largura = img.shape[1] // 2
img = cv2.resize(img, (largura, altura))

# 4. Criar máscara para ignorar partes pretas
mask = cv2.inRange(img, (0,0,0), (40,40,40))  # faixa do preto
mask_inv = cv2.bitwise_not(mask)  # inverte para pegar partes NÃO pretas

# 5. Converter imagem para escala de cinza para medir brilho
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 6. Extrair apenas pixels válidos (não pretos)
pixels_validos = gray[mask_inv > 0]

# 7. Definir faixas de brilho
#   - Escuro: 0–85
#   - Médio: 86–170
#   - Claro: 171–255
escuros = np.sum(pixels_validos <= 85)
medios = np.sum((pixels_validos > 85) & (pixels_validos <= 170))
claros = np.sum(pixels_validos > 170)
total = len(pixels_validos)

# 8. Calcular porcentagens
p_escuros = (escuros / total) * 100
p_medios = (medios / total) * 100
p_claros = (claros / total) * 100

print(f"Porcentagem de áreas escuras: {p_escuros:.2f}%")
print(f"Porcentagem de áreas médias:  {p_medios:.2f}%")
print(f"Porcentagem de áreas claras:  {p_claros:.2f}%")

# 9. Exibir gráfico de barras
categorias = ["Escuras", "Médias", "Claras"]
valores = [p_escuros, p_medios, p_claros]
cores = ["#2c3e50", "#95a5a6", "#ecf0f1"]

plt.figure(figsize=(6,4))
plt.bar(categorias, valores, color=cores)
plt.title("Distribuição de Brilho (sem partes pretas)")
plt.ylabel("Porcentagem (%)")
plt.ylim(0, 100)
for i, v in enumerate(valores):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', fontweight='bold')
plt.show()
