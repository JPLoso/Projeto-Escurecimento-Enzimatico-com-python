import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_imagem(entrada_imagem):
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.PNG *.jpg *.JPG *.jpeg *.JPEG *.bmp *.BMP")]
    )
    if caminho:
        entrada_imagem.set(caminho)