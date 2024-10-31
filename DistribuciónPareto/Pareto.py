import pandas as pd
import matplotlib.pyplot as plt                 # Gaficar
import numpy as np                              
from scipy.stats import pareto, kurtosis, skew  # Libreria para calculo de estadistica

# Cargar datos
data_path = 'C:\\Users\\Personal\\Desktop\\Probabilidad\\Probabilidad\\DistribucionPareto\\kaggle_income.csv'
df = pd.read_csv(data_path, encoding='latin1')

# Usar la columna 'Mean' para representar los ingresos
income_data = df['Mean'].dropna()

# Ajustar los datos a una distribución de Pareto
shape_param = 2 
fitted_pareto = pareto.fit(income_data, floc=0)

# Graficar los datos y la distribución ajustada
plt.figure(figsize=(10, 6))
count, bins, _ = plt.hist(income_data, bins=50, density=True, alpha=0.6, color='skyblue', label="Datos de ingresos")
plt.plot(bins, pareto.pdf(bins, *fitted_pareto), 'r--', linewidth=2, label="Ajuste de Pareto")
plt.title("Distribución de Ingresos - Aproximación de Pareto")
plt.xlabel("Ingresos Promedio")
plt.ylabel("Densidad de Frecuencia")
plt.legend()

# Calcular medidas estadísticas
mean = np.mean(income_data)
median = np.median(income_data)
mode = income_data.mode()[0] if not income_data.mode().empty else None
variance = np.var(income_data)
std_dev = np.std(income_data)
range_data = np.ptp(income_data)
skewness = skew(income_data)
kurt = kurtosis(income_data)

# Mostrar estadísticas en la gráfica
stats_text = (
    f"Media: {mean:.2f}\n"
    f"Mediana: {median:.2f}\n"
    f"Moda: {mode:.2f}\n"
    f"Varianza: {variance:.2f}\n"
    f"Desviación Estándar: {std_dev:.2f}\n"
    f"Rango: {range_data:.2f}\n"
    f"Asimetría: {skewness:.2f}\n"
    f"Curtosis: {kurt:.2f}"
)
plt.text(0.95, 0.6, stats_text, fontsize=10, transform=plt.gca().transAxes,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.8))

plt.show()
