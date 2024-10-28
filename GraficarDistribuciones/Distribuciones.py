import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import poisson, binom, geom

# Parámetros de las distribuciones
n_values = [5, 20]  # Valores de n para comparar
p = 0.5             # Probabilidad de éxito
lambda_ = 5         # Parámetro lambda para Poisson

# Valores de x para las array de las distribuciones
x_poisson = np.arange(0, 20)
x_binom = np.arange(0, max(n_values) + 1)
x_geom = np.arange(1, 20)

# Crear la figura y titulos
fig, axs = plt.subplots(3, 2, figsize = (12, 10))
fig.suptitle('Distribuciones Poisson, Binomial y Geométrica con diferentes valores de n')

# Distribución Poisson
for i, n in enumerate(n_values):
    pmf_poisson = poisson.pmf(x_poisson, lambda_)
    axs[0, i].stem(x_poisson, pmf_poisson, basefmt=" ") 
    axs[0, i].set_title(f'Distribución Poisson (λ={lambda_})')
    axs[0, i].set_xlabel('k')
    axs[0, i].set_ylabel('P(X=k)')

# Distribución Binomial
for i, n in enumerate(n_values):
    pmf_binom = binom.pmf(x_binom, n, p)
    axs[1, i].stem(x_binom, pmf_binom, basefmt=" ")
    axs[1, i].set_title(f'Distribución Binomial (n={n}, p={p})')
    axs[1, i].set_xlabel('k')
    axs[1, i].set_ylabel('P(X=k)')

# Distribución Geométrica
for i, n in enumerate(n_values):
    pmf_geom = geom.pmf(x_geom, p)
    axs[2, i].stem(x_geom, pmf_geom, basefmt=" ")
    axs[2, i].set_title(f'Distribución Geométrica (p={p})')
    axs[2, i].set_xlabel('k')
    axs[2, i].set_ylabel('P(X=k)')

# Imprimir la grafica:
plt.tight_layout(rect=[0, 0, 1, 0.96]) #Ajuste de las graficas al espacio
plt.show()