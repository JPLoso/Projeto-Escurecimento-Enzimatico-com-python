from calc_percentual import calc_percentuais
import cv2

def analisar_imagem(img, mask):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return calc_percentuais(mask, gray)