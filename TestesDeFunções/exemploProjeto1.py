import matplotlib.pyplot as plt

# Dados
horas = ["00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h",
         "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"]
porcentagem = [5, 7, 6, 8, 10, 12, 20, 30, 50, 55, 60, 65, 70, 75, 80, 85, 80, 70, 60, 50, 40, 30, 15, 10]

# Criar gráfico de barras
plt.bar(horas, porcentagem, color='skyblue')

# Títulos e rótulos
plt.title("Porcentagem por Hora")
plt.xlabel("Hora do dia")
plt.ylabel("Porcentagem (%)")
plt.ylim(0, 100)  # garante que o eixo Y vá de 0 a 100%

# Rotacionar os labels do eixo X para caber melhor
plt.xticks(rotation=45)

# Mostrar grade e gráfico
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # ajusta layout para não cortar labels
plt.show()
