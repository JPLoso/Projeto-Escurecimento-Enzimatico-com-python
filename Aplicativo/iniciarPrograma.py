from tkinter import messagebox
from gerarGrafico import gerarGrafico

def iniciar_programa(entrada_imagem):
    caminho = entrada_imagem.get()
    if caminho.strip() == "":
        messagebox.showwarning("Atenção", "Nenhuma imagem selecionada!")
    else:
        try:
            gerarGrafico(caminho)
            messagebox.showinfo("Sucesso", "Gráfico gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
