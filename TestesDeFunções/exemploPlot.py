import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.plot(x, y, color='red', marker='o', linestyle='--')
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de exemplo")
plt.show()  