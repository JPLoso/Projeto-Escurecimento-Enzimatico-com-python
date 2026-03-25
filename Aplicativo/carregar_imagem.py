import numpy as np
import cv2
from PIL import Image

def carregar_imagem(caminho):
    img_pil = Image.open(caminho).convert("RGB")
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)