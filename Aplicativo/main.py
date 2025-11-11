import tkinter as tk
from tkinter import filedialog, messagebox
from gerarGrafico import gerarGrafico

def selecionar_imagem():
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.PNG *.jpg *.JPG *.jpeg *.JPEG *.bmp *.BMP")]
    )
    if caminho:
        entrada_imagem.set(caminho)

def iniciar_programa():
    caminho = entrada_imagem.get()
    if caminho.strip() == "":
        messagebox.showwarning("Atenção", "Nenhuma imagem selecionada!")
    else:
        try:
            gerarGrafico(caminho)
            messagebox.showinfo("Sucesso", "Gráfico gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar janela
janela = tk.Tk()
janela.title("Analisador de Imagem")
janela.geometry("500x180")

entrada_imagem = tk.StringVar()

tk.Label(janela, text="Selecione uma imagem para análise:").pack(pady=5)

tk.Entry(janela, textvariable=entrada_imagem, width=50).pack(pady=5)

tk.Button(janela, text="Buscar Imagem", command=selecionar_imagem).pack(pady=5)

tk.Button(janela, text="Iniciar Programa", command=iniciar_programa).pack(pady=10)

janela.mainloop()
