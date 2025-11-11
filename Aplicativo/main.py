from gerarGrafico import gerarGrafico
from iniciarPrograma import iniciar_programa
from selecionarImagem import selecionar_imagem
import tkinter as tk

# Criar janela
janela = tk.Tk()
janela.title("Analisador de Imagem")
janela.geometry("500x180")

entrada_imagem = tk.StringVar()

tk.Label(janela, text="Selecione uma imagem para análise:").pack(pady=5)

tk.Entry(janela, textvariable=entrada_imagem, width=50).pack(pady=5)

tk.Button(janela, text="Buscar Imagem", command=selecionar_imagem(entrada_imagem)).pack(pady=5)

tk.Button(janela, text="Iniciar Programa", command=iniciar_programa(entrada_imagem)).pack(pady=10)

janela.mainloop()
