import random
import statistics
import matplotlib.pyplot as plt

# Generar 60 números aleatorios entre 1 y 100
numeros = [random.randint(10, 99) for _ in range(60)]
print("Números generados:")
print(numeros)

# Ordenar la lista
numeros_ordenados = sorted(numeros)

# Cálculos estadísticos
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.mode(numeros)
rango = max(numeros) - min(numeros)
varianza = statistics.variance(numeros)
desviacion_estandar = statistics.stdev(numeros)

# Mostrar estadísticas
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Rango: {rango}")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación estándar: {desviacion_estandar:.2f}")

# Gráfico de barras
plt.figure(figsize=(10, 4))
plt.hist(numeros, bins=10, color='skyblue', edgecolor='black')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Media: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1.5, label=f'Mediana: {mediana}')
plt.axvline(moda, color='purple', linestyle='dashed', linewidth=1.5, label=f'Moda: {moda}')
plt.title('Distribución de los números aleatorios')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de caja (boxplot) para ver la dispersión
plt.figure(figsize=(5, 4))
plt.boxplot(numeros, vert=False)
plt.title('Diagrama de caja (Boxplot)')
plt.xlabel('Valores')
plt.tight_layout()
plt.show()