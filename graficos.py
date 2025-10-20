import matplotlib.pyplot as plt

# Datos de ejemplo: cantidad de vehículos generados por dirección
vehiculos_por_direccion = {
    'Derecha': 50,
    'Abajo': 30,
    'Izquierda': 40,
    'Arriba': 20
}

# Convertimos los datos en listas para graficar
direcciones = list(vehiculos_por_direccion.keys())
cantidad_vehiculos = list(vehiculos_por_direccion.values())

# Crear el histograma
plt.bar(direcciones, cantidad_vehiculos, color='skyblue', edgecolor='black')

# Añadir título y etiquetas
plt.title('Cantidad de Vehículos por Dirección')
plt.xlabel('Dirección')
plt.ylabel('Cantidad de Vehículos')

# Mostrar el gráfico
plt.show()


import matplotlib.pyplot as plt

# Datos de ejemplo: cantidad de vehículos por fase del semáforo
vehiculos_por_fase = {
    'Fase 1': 120,
    'Fase 2': 150,
    'Fase 3': 100,
    'Fase 4': 130
}

# Convertimos los datos en listas para graficar
fases = list(vehiculos_por_fase.keys())
cantidad_vehiculos = list(vehiculos_por_fase.values())

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(fases, cantidad_vehiculos, color='lightcoral', edgecolor='black')

# Añadir título y etiquetas
plt.title('Cantidad de Vehículos por Fase del Semáforo')
plt.xlabel('Fase del Semáforo')
plt.ylabel('Cantidad de Vehículos')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Datos de ejemplo: tiempo en segundos que cada semáforo permanece en verde
tiempo_verde_fases = {
    'Fase 1': 25,
    'Fase 2': 30,
    'Fase 3': 20,
    'Fase 4': 15
}

# Convertimos los datos en listas para graficar
fases = list(tiempo_verde_fases.keys())
tiempos_verde = list(tiempo_verde_fases.values())

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(tiempos_verde, labels=fases, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightblue', 'lightcoral', 'lightyellow'], shadow=True)

# Añadir título
plt.title('Distribución del Tiempo de Semáforo en Verde por Fase')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Datos de ejemplo: horas del día y número de vehículos registrados
horas = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
vehiculos = np.array([50, 60, 80, 100, 120, 130, 110, 90, 70, 60, 80, 150, 200, 180, 160])

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(6, 20)
ax.set_ylim(0, 250)
ax.set_xlabel('Hora del Día')
ax.set_ylabel('Número de Vehículos')
ax.set_title('Aumento del Tráfico Vehicular a lo Largo del Día')

# Inicializar el gráfico de dispersión con un arreglo vacío de forma (0, 2)
scatter = ax.scatter([], [], color='blue')

# Función de inicialización
def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

# Función de actualización para la animación
def update(frame):
    x = horas[:frame]
    y = vehiculos[:frame]
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(horas) + 1, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Datos de ejemplo: tiempo en verde que cada dirección tuvo en una simulación
tiempo_verde_por_direccion = {
    'Derecha': 30,
    'Abajo': 45,
    'Izquierda': 25,
    'Arriba': 40
}

# Convertir a listas
direcciones = list(tiempo_verde_por_direccion.keys())
tiempos = list(tiempo_verde_por_direccion.values())

# Crear gráfico de barras horizontales
plt.figure(figsize=(8, 5))
plt.barh(direcciones, tiempos, color='seagreen', edgecolor='black')
plt.xlabel('Tiempo en Verde (segundos)')
plt.title('Tiempo de Semáforo en Verde por Dirección')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Supongamos que recuperas estos valores durante la simulación
# (duraciones reales acumuladas por fase en cada dirección)
tiempos_fases = {
    'Derecha': {'Verde': 30, 'Amarillo': 5, 'Rojo': 35},
    'Abajo':   {'Verde': 45, 'Amarillo': 5, 'Rojo': 50},
    'Izquierda': {'Verde': 25, 'Amarillo': 5, 'Rojo': 30},
    'Arriba':  {'Verde': 40, 'Amarillo': 5, 'Rojo': 45}
}

# Preparar los datos para graficar
direcciones = list(tiempos_fases.keys())
verde = [tiempos_fases[d]['Verde'] for d in direcciones]
amarillo = [tiempos_fases[d]['Amarillo'] for d in direcciones]
rojo = [tiempos_fases[d]['Rojo'] for d in direcciones]

import numpy as np
x = np.arange(len(direcciones))
ancho = 0.2

# Graficar barras apiladas horizontalmente
plt.figure(figsize=(10, 6))
plt.bar(x - ancho, verde, width=ancho, color='green', label='Verde')
plt.bar(x, amarillo, width=ancho, color='yellow', label='Amarillo')
plt.bar(x + ancho, rojo, width=ancho, color='red', label='Rojo')

plt.xticks(x, direcciones)
plt.ylabel('Duración (segundos)')
plt.title('Duración de cada fase del semáforo por dirección')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo: tiempos de espera acumulados por dirección en cada ciclo
tiempos_espera = {
    'Derecha': [5, 6, 7, 8, 9],
    'Abajo': [4, 5, 6, 7, 8],
    'Izquierda': [3, 4, 5, 6, 7],
    'Arriba': [2, 3, 4, 5, 6]
}

# Preparar los datos para graficar
ciclos = np.arange(1, len(tiempos_espera['Derecha']) + 1)

# Crear el gráfico
plt.figure(figsize=(10, 6))
for direccion, tiempos in tiempos_espera.items():
    plt.plot(ciclos, tiempos, label=f'Dirección {direccion}')

# Añadir etiquetas y título
plt.xlabel('Ciclo Semafórico')
plt.ylabel('Tiempo de Espera Acumulado (segundos)')
plt.title('Variabilidad del Tiempo de Espera por Dirección')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar el gráfico
plt.show()


