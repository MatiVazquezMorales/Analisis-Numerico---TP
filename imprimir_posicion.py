import matplotlib.pyplot as plt
from imprimir_velocidades import *
from tp import *


# Definir el índice inicial para t > 1
start_idx = int(1 / h)  # Índice donde comienza el análisis


plt.figure(figsize=(12, 10))

plt.subplot(2, 1, 1)
colors = plt.cm.tab10(np.linspace(0, 1, n + 1))  # Paleta de colores
for i in range(n+1):
    if i == 0:
        plt.plot(t, z[i, :], label=f'Parte de adelante del vehiculo {i}', color="black")
        plt.plot(t, z[i, :] - L, label=f'Parte de atras del vehiculo {i}', color="black")
    if i == 12:
        plt.plot(t, z[i, :], label=f'Parte de adelante del vehiculo {i}', color="purple")
        plt.plot(t, z[i, :] - L, label=f'Parte de atras del vehiculo {i}', color="purple")
    elif i == n:
        plt.plot(t, z[i, :], label=f'Parte de adelante del vehiculo {i}', color="brown")
        plt.plot(t, z[i, :] - L, label=f'Parte de atras del vehiculo {i}', color="brown")
    else:
        plt.plot(t, z[i, :], label=f'Parte de adelante del vehiculo {i}', color=colors[i])
        plt.plot(t, z[i, :] - L, label=f'Parte de atras del vehiculo {i}', color=colors[i])
plt.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición relativa (m)')
plt.title('Posiciones relativas de los vehículos')
plt.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=3)  # Legenda debajo, con 3 columnas
plt.tight_layout()
#plt.legend()
plt.yticks(range(-(n+2)*(L+d), 1, L+d))

plt.tight_layout()
plt.show()