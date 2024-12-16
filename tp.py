import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constantes
vc = 25  # Velocidad de crucero (m/s)
n = 14  # Número de vehículos
L = 5  # Longitud del vehículo (m)
d = 10  # Distancia entre vehículos (m)
T = 60  # Tiempo total en segundos
h = 0.1  # Tamaño del paso de tiempo
k = 1.5  # Factor de perturbación
t1 = 0.2  # Tiempo característico de la perturbación
C = 9.375  # Constante del sistema
tau = 1  # Retardo en la reacción de los vehículos

# Número de pasos de tiempo
n_pasos = int(T / h) + 1
t = np.linspace(0, T, n_pasos)

# perturbacion de velocidad
def velocidad_perturbacion(t):
    return -k * vc * t * np.exp((t1 - t) / t1)

# perturbacion de posicion
def posicion_perturbacion(t):
    return -k * vc * t1 * np.e * (t1 - np.exp(-t / t1) * (t + t1))

# derivada para la velocidad del vehiculo i
def derivada_velocidad(vehiculo_indx, tiempo_actual, posicion_historica):
    if tiempo_actual <= vehiculo_indx * tau:
        return 0

    # tiempo de delay
    delay_index = int((tiempo_actual - tau) / h)
    if delay_index < 0:
        return 0

    posicion_actual = posicion_historica[vehiculo_indx, delay_index]
    posicion_anterior = posicion_historica[vehiculo_indx - 1, delay_index]

    posicion_ratio = (posicion_actual - posicion_anterior) / -(L + d)
    if posicion_ratio <= 0:
        return 0
    return C * np.log(posicion_ratio)

# Inicializacion de arrays
posiciones = np.zeros((n + 1, n_pasos))
velocidades = np.full((n + 1, n_pasos), np.nan)  # Crear matriz llena de NaN
velocidades[:, 0] = 25  # Asignar 25 a la primera columna

# Condiciones iniciales
for vehiculo_indx in range(n + 1):
    posiciones[vehiculo_indx, 0] = -vehiculo_indx * (L + d)

# Metodo de euler
for paso_index in range(1, n_pasos):
    tiempo_actual = t[paso_index]

    # Actualizacion posicion de los vehiculos con perturbacion
    posiciones[0, paso_index] = posicion_perturbacion(tiempo_actual)

    # Actualizacion de posicion de vehiculos siguientes
    for vehiculo_indx in range(1, n + 1):
        velocidad_derivada = derivada_velocidad(vehiculo_indx, tiempo_actual, posiciones)
        posiciones[vehiculo_indx, paso_index] = posiciones[vehiculo_indx, paso_index - 1] + h * velocidad_derivada

# velocidades
# Perturbacion velocidades
velocidades[0, :] = velocidad_perturbacion(t) + vc

# vehiculos siguientes
for vehiculo_indx in range(1, n + 1):
    velocidades[vehiculo_indx, 1:] = (posiciones[vehiculo_indx, 1:] - posiciones[vehiculo_indx, :-1]) / h + vc

# dataframes para posiciones y velocidades
posicion_df = pd.DataFrame(posiciones.T, columns=[f"vehiculo {i}" for i in range(n + 1)])
velocidad_df = pd.DataFrame(velocidades.T, columns=[f"vehiculo {i}" for i in range(n + 1)])

# Calcular velocidades mínimas y máximas para cada vehículo
min_max_velocidades = velocidad_df.aggregate(['min', 'max'])

# Mostrar resultados
for vehiculo in velocidad_df.columns:
    min_vel = min_max_velocidades.loc['min', vehiculo]
    max_vel = min_max_velocidades.loc['max', vehiculo]
    print(f"{vehiculo}: Velocidad mínima = {min_vel:.2f} m/s, Velocidad máxima = {max_vel:.2f} m/s")

