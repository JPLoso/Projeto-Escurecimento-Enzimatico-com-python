import cv2
import matplotlib.pyplot as plt
from PIL import Image
from calc_percentual import calc_percentuais

def gerarGrafico(entrada):
    saida = "imagem_convertida.png"
    img_pil = Image.open(entrada).convert("RGB")
    img_pil.save(saida)
    img = cv2.imread(saida)

    if img is None:
        print("Erro ao carregar")
        exit()

    # Reduz tamanho opcional
    altura = img.shape[0] // 2
    largura = img.shape[1] // 2
    img = cv2.resize(img, (largura, altura))

    # Máscara para ignorar preto
    mask = cv2.inRange(img, (0,0,0), (40,40,40))
    mask_inv = cv2.bitwise_not(mask)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- Dividir imagem em duas regiões ---
    meio = img.shape[1] // 2
    regioes = {
        "Parte Esquerda": (slice(None), slice(0, meio)),
        "Parte Direita": (slice(None), slice(meio, img.shape[1]))
    }

    # --- Analisar cada região separadamente ---
    resultados = {} 
    for nome, (ys, xs) in regioes.items():
        sub_gray = gray[ys, xs]
        sub_mask = mask_inv[ys, xs]
        resultados[nome] = calc_percentuais(sub_mask, sub_gray)

    # --- Plotar ---
    categorias = ["Escuras", "Médias", "Claras"]
    cores = ["#2c3e50", "#95a5a6", "#ecf0f1"]

    fig, axes = plt.subplots(1, 2, figsize=(10,4), sharey=True)
    for ax, (nome, valores) in zip(axes, resultados.items()):
        ax.bar(categorias, valores, color=cores)
        ax.set_title(nome)
        ax.set_ylim(0,100)
        for i, v in enumerate(valores):
            ax.text(i, v+1, f"{v:.1f}%", ha='center', fontweight='bold')
    plt.suptitle("Distribuição de Brilho por Região")
    plt.show()