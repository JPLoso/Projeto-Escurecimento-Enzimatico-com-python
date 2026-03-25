import cv2
import numpy as np

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