
```python
import matplotlib.pyplot as plt

# Dados
horas = ["00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h", "09h", "10h", "11h", "12h", "13h", "14h", "15h", "16h", "17h", "18h", "19h", "20h", "21h", "22h", "23h"] # Valores do gráfico X

porcentagem = [5, 7, 6, 8, 10, 12, 20, 30, 50, 55, 60, 65, 70, 75, 80, 85, 80, 70, 60, 50, 40, 30, 15, 10]# valores do gráfico Y
  
# Criar gráfico de barras
plt.bar(horas, porcentagem, color='skyblue')

# Adicionar valores no topo das barras
for i, valor in enumerate(porcentagem):
plt.text(i, valor + 1, f"{valor}%", ha='center', va='bottom', fontsize=8)

# Títulos e rótulos
plt.title("Porcentagem por Hora")
plt.xlabel("Hora do dia")
plt.ylabel("Porcentagem (%)")
plt.ylim(0, 100) # limita o y de 0% a 100%
plt.xticks(rotation=45) #Rotaciona os números do x para 45 graus
plt.grid(axis='y', linestyle='--', alpha=0.7) #Adiciona grade no grafico, sai apenas do Y, com um estilo de linha --, e com uma visibilidade 0.7
plt.tight_layout()# para não se sobrepor
plt.show()
```

#ylim ->limita os valores de y (min, max)
#xticks -> Seleciona os números dos X. #rotate Faz a ação de rotacionar os números
#gridx -> Faz a grade

Ideias:
 #for em horas e porcentagem para montar o gráfico, em que o usuário adicione o valor.