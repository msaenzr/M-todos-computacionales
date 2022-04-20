import pandas as pd
import numpy as np

""" 
A manera de ejemplo, tomaremos 3 puntos y hallaremos el polinomio de Lagrange asociado a dichos puntos (P vs T). Así mismo hallaremos el polinomio asociado por sympy. +10 puntos.
Tabla Interpolación de P vs T, utilizando valores intermedios de temperatura. Para esto generalice el programa del punto 1. +15
Tabla Interpolación de sg vs T.+5
Tabla Interpolación de sf vs T.+5
Gráficas en formato png.  Los ejes deben aparecer debidamente identificados y el tamaño de las etiquetas debe ser visible. +10
Análisis de resultados y conclusiones. +5
"""

#Ejemplo con tres puntos escogidos de la tabla A-4.

#Implementación con Numpy.
X = np.array([205,210,215])
Y = np.array([1274.3,1907.7,2105.9])

data = pd.read_csv("vapor_saturado.csv",delimiter=";")

def l_0(x,X):
    return (x-X[1])*(x-X[2])/((X[0]-X[1])*(X[0]-X[2]))

def l_1(x,X):
    return (x-X[0])*(x-X[2])/((X[1]-X[0])*(X[1]-X[2]))

def l_2(x,X):
    return (x-X[0])*(x-X[1])/((X[2]-X[0])*(X[2]-X[1]))

def p_lagrange(x,X,Y):
    return l_0(x,X)*Y[0]+l_1(x,X)*Y[1]+l_2(x,X)*Y[2]

#Prueba del ejemplo
print(p_lagrange(212.5,X,Y))

#Implementación con Sympy.

#Generalización método polinomios de Lagrange.


