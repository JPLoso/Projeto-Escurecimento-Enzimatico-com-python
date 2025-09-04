import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)  # cria uma grade 2x2 de subplots

ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 0].set_title("Subplot 1")

ax[0, 1].plot([1, 2, 3], [2, 4, 6])
ax[0, 1].set_title("Subplot 2")

ax[1, 0].plot([1, 2, 3], [3, 2, 1])
ax[1, 0].set_title("Subplot 3")

ax[1, 1].plot([1, 2, 3], [6, 4, 2])
ax[1, 1].set_title("Subplot 4")

plt.tight_layout()  # ajusta os subplots para não se sobreporem
plt.show()
