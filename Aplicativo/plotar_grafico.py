from matplotlib.pyplot import plot as plt

def plotar_grafico(valores):
    categorias = ["Escuras", "Médias", "Claras"]

    plt.figure(figsize=(6,4))
    plt.bar(categorias, valores)

    for i, v in enumerate(valores):
        plt.text(i, v+1, f"{v:.1f}%", ha='center')

    plt.ylim(0,100)
    plt.title("Distribuição de claridade")
    plt.ylabel("% dos Pixels")
    plt.show()