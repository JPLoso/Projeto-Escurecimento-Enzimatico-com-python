import matplotlib.pyplot as plt # importa a o pyplot com o apelido de plt do matplotlib

fig = plt.figure(figsize=(6, 4))  # cria uma figura de 6x4 polegadas
ax = fig.add_axes([0.1, 0.1, 0.5, 0.5])  # [esq, baixo, largura, altura]
ax.plot([1, 2, 3], [4, 5, 6])  # cria o gráfico dentro do eixo
plt.show()
