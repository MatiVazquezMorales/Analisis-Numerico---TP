import matplotlib.pyplot as plt
from tp import *

# Datos generados en el segundo código
z = posiciones
v = velocidades

plt.figure(figsize=(12, 10))

# Gráfica de posiciones
plt.subplot(2, 1, 1)
for i in range(n + 1):
    plt.plot(t, z[i, :], label=f'Vehículo {i}')
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición relativa (m)')
plt.title('Posiciones relativas de los vehículos')
plt.legend()
plt.yticks(range(int(-(n+2)*(L+d)), 1, int(L+d)))  # Convertimos a enteros para range

# Gráfica de velocidades
plt.subplot(2, 1, 2)
for i in range(n + 1):
    plt.plot(t, v[i, :], label=f'Vehículo {i}')
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidades de los vehículos')
plt.legend()

plt.tight_layout()
plt.show()