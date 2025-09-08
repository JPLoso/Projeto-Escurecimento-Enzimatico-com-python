import matplotlib.pyplot as plt

# Dados
valores = None
controler = 1
horas = []
porcentagem = []

print("Digite próximo para ir para os valores de Y\n")
print("Digite Mostrar para ir para o gráfico")
while(True):
    if controler == 1:
        valores = input("Digite o valor de X: ")
        if valores in "Próximo" or valores in "próximo":
            controler = 2
        else:
            horas.append(valores)
    elif controler == 2:
        valores = str(input("Digite o valor de Y: "))
        if valores in "Mostrar" or valores in "mostrar":
            controler = 3   
        else:
            porcentagem.append(int(valores))
    else:
        break

# Criar gráfico de barras
plt.bar(horas, porcentagem, color='skyblue')

# Adicionar valores no topo das barras
for i, valor in enumerate(porcentagem):
    plt.text(i, valor + 1, f"{valor}%", ha='center', va='bottom', fontsize=8)

# Títulos e rótulos
plt.title("Porcentagem por Hora")
plt.xlabel("Hora do dia")
plt.ylabel("Porcentagem (%)")
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
