"""
    UNIVERSIDAD SERGIO ARBOLEDA

    Nombre: Valentina Del Pilar Franco Suárez

    Correo: valentina.franco01@correo.usa.edu.co

    Docente: Jonh Jairo Corredor

    Fecha: 05 de mayo del 2021

    Ciudad: Bogotá D.C.

    TALLER RENDIMIENTO CYTHON/PYTHON
"""
from functionE import rbf_network
import cyfunctionE 
import numpy as np
import time
import matplotlib.pyplot as plt

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

inicio = time.time()
rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio

inicio = time.time()
cyfunctionE.rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio

speedUp = round(tiempoPy/tiempoCy,3)

print(f'Tiempo Python : {tiempoPy}\n')
print(f'Tiempo Cython: {tiempoCy}\n')
print("SpeedUp: {}\n".format(speedUp))

fig, ax = plt.subplots()
etiquetas = ["Tiempo python", "Tiempo Cython"]
tiempos = [tiempoPy, tiempoCy]

ax.set_ylabel("Tiempo")
plt.bar(etiquetas, tiempos, width=0.3, color=["thistle", "lightblue"], align='center')
plt.savefig('grafica.png')
plt.grid()
plt.show()