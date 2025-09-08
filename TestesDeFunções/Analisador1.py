import cv2
import numpy as np

print(cv2.__version__)
# Carregar a imagem
img = cv2.imread("/home/joao-pedro-veloso/Documentos/ProjetoEngenhariaAlimentos/TestesDeFunções/maca.jpg")

altura = img.shape[0]
largura = img.shape[1]



print(altura)
print(largura)

print(img.shape)

mask = cv2.inRange(img, (0,0,0), (40,40,40))

cv2.imshow("Mascara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()