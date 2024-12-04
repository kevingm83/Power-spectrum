import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k
from scipy.integrate import simps

# Constantes
T = 5700  # Temperatura en Kelvin

# Rango de longitudes de onda para el espectro visible
wavelengths = np.linspace(380.000000000000e-9, 750.000000000000e-9, 1000)  # de 380 nm a 750 nm

# Ley de Planck
def planck_law(lambda_, T):
    exponent = (h * c) / (lambda_ * k * T)
    return (2 * h * c**2) / (lambda_**5) / (np.exp(exponent) - 1)

# Calcular intensidades para el rango visible
intensities = planck_law(wavelengths, T)

# Integrar para encontrar la energía total emitida en el rango visible
total_energy = simps(intensities, wavelengths)

# Visualización del espectro de cuerpo negro
plt.figure(figsize=(10, 5))
plt.plot(wavelengths * 1e9, intensities, color='blue', label=f'Temperature = {T}K')
plt.title('Espectro de Cuerpo Negro en el Rango Visible')
plt.xlabel('Longitud de onda (nm)')
plt.ylabel('Intensidad (W/m^3)')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar la energía total integrada
print(f"La energía total integrada sobre el rango visible (380 nm a 750 nm) es: {total_energy:.4e} W/m^2")
print(intensities)
