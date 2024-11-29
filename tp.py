import numpy as np
import matplotlib.pyplot as plt
import math

# Parámetros
vc = 25  # Velocidad de crucero (m/s)
num_vehiculos = 10  # Número de vehículos
L = 5  # Longitud del vehículo (m)
d = 10  # Distancia entre vehículos (m)
tiempo_total = 60  # Tiempo total en segundos
h = 0.1  # Tamaño del paso de tiempo
t = np.arange(0, tiempo_total + h, h)  # Rango de tiempo
k = 1.5  # Factor de perturbación
t_1 = 0.2  # Tiempo característico de la perturbación
C = 9.375  # Constante del sistema
tau = 1  # Retardo en la reacción de los vehículos

# Inicialización de matrices
z = np.zeros((num_vehiculos, len(t)))  # Matriz para posiciones
v = np.full((num_vehiculos, len(t)), 0)  # Velocidades iniciales constantes

# Condiciones iniciales de posiciones
for j in range(num_vehiculos):
    z[j, 0] = -j * (L + d)  # Posiciones iniciales separadas por L + d

# Calcular las posiciones y velocidades en todo el tiempo
for i in range(1, len(t)):  # Iterar sobre el tiempo
    for j in range(num_vehiculos):  # Iterar sobre los vehículos
        if j == 0:
            # Perturbación en el primer vehículo
            perturbacion = -k * vc * t[i] * math.exp((t_1 - t[i]) / t_1)
            v[j, i] = perturbacion  # Velocidad del vehículo 0
            z[j, i] = -k * vc * t_1 * math.e * math.exp((t_1 - math.exp(-t[i] / t_1) * (t[i] + t_1)))# Posición del vehículo 0

        else:

            if i <= j * tau:
                v[j, i] = 0
                z[j, i] = z[j, i-1]
            
            else:
                distancia = z[j, i-tau] - z[j-1, i - tau]
                v[j, i] = C * math.log(abs(distancia/-(L + d)))
                z[j, i] = z[j, i-1] + h * v[j, i]           

# Graficar las posiciones de los vehículos
plt.figure(figsize=(12, 6))
for j in range(num_vehiculos):
    plt.plot(t, z[j, :], label=f'Vehículo {j}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Posición de los vehículos en función del tiempo')
plt.legend()
plt.grid(True)
plt.show()

# Graficar las velocidades de los vehículos
plt.figure(figsize=(12, 6))
for j in range(num_vehiculos):
    plt.plot(t, v[j, :], label=f'Vehículo {j}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad de los vehículos en función del tiempo')
plt.legend()
plt.grid(True)
plt.show()

# Calcular y mostrar velocidades mínimas y máximas
print("\nVelocidades mínimas y máximas por vehículo:")
for i in range(num_vehiculos):
    velocidad_min = np.min(v[i, :])
    velocidad_max = np.max(v[i, :])
    print(f"Vehículo {i+1}: Velocidad mínima = {velocidad_min:.2f} m/s, Velocidad máxima = {velocidad_max:.2f} m/s")

for j in range(num_vehiculos):
    print(f"vehiculo: {j}")
    print(v[j,:])

