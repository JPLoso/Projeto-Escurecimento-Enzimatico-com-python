from tkinter import filedialog

def selecionar_imagem(entrada_imagem):
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.PNG *.jpg *.JPG *.jpeg *.JPEG *.bmp *.BMP")]
    )
    if caminho:
        entrada_imagem.set(caminho)