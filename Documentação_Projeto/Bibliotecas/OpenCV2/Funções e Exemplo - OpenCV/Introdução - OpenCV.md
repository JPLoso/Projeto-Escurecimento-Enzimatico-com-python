Como funciona:
- Abre a imagem com **cv2.imread()** como **matrizNumpy**
- #matrizNumpy:
	- Cada pixel tem 3 valores: #BRG **(Blue, Green, Red)**
		- (0, 0 ,0) - > Preto
		- (255, 255, 255) -> Branco
		- (0, 0 , 255) -> Vermelho
	- Tamanho da imagem é: **Altura x Largura x 3**

Exemplo:

```python
imagem = cv2.imread("Foto.jpg")
print(imagem.shape)
```
Saída:

```python
(1080, 1920, 3)   # 1080 pixels de altura, 1920 de largura, 3 canais (BGR)
```

#imread -> Lê a imagem e transforma em uma matrizNumpy
#shape -> Pega as medidas da imagem (Altura, Largura e Canais de Cores)

------------------------------------------------------------------------



