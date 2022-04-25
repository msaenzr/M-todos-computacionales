from cProfile import label
from symtable import Symbol
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random as rd

#Ejemplo con tres puntos escogidos de la tabla A-4.

#Implementación con Numpy.
X = np.array([205,210,215])
Y = np.array([1274.3,1907.7,2105.9])
#data ={'T':[205,210,215], 'Psat':[1274.3,1907.7,2105.9]}
#data = {'T':[-1.5,-0.75,0,0.75,1.5], 'Psat':[-14.1014,-0.931596,0,0.931596,14.1014]}
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
print("Prueba de la interpolación con x = 212.5: ")
print(p_lagrange(212.5,X,Y))

#Implementación con Sympy.

x = sp.Symbol('x')
p_l= p_lagrange(x,X,Y)
p_e = sp.expand(p_l)
print("\nPolinomio de Lagrange: ")
print(p_l)
print("\nExpansión del polinomio de Lagrange: ")
print(p_e)

#Generalización método polinomios de Lagrange respecto a la tabla A-4.

#Algoritmo para obtener la interpolación con el polinomio de Lagrange.
def p_lagrange(data,x,key_1,key_2):
    p_l=1
    for j in range(len(data[key_1])):
        l_i=1
        for i in range(len(data[key_1])):
            if i!=j:
                x_i = data[key_1][i]
                x_j = data[key_1][j]
                l_i *= (x-x_i)/(x_j-x_i)
        y_j = data[key_2][j]
        p_l+=(y_j*l_i)
    return p_l

#Algoritmo para obtener 50 datos aleatorios entre los rangos escogidos para cada interpolación.

def datos_intermedios(data,min,max,key_1,key_2):
    l_x=[]
    l_y=[]
    for n in range(3):
        x = rd.randint(min,max)
        y = p_lagrange(data,x,key_1,key_2)
        l_x.append(x)
        l_y.append(y)
    return (l_x,l_y)

# Análisis tabla Interpolación de P vs T

dat = datos_intermedios(data,0,373,'T','Psat')
print(dat)
print(p_lagrange(data,35,'T','Psat'))
plt.plot(data['T'],data['Psat'],c='Violet')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de P vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Presión Saturada (KPa)")
plt.scatter(dat[0],dat[1],c='Black')
plt.show()

"""Tabla Interpolación de P vs T, utilizando valores intermedios de temperatura. Para esto generalice el programa del punto 1. +15"
Tabla Interpolación de sg vs T.+5
Tabla Interpolación de sf vs T.+5
Gráficas en formato png.  Los ejes deben aparecer debidamente identificados y el tamaño de las etiquetas debe ser visible. +10
Análisis de resultados y conclusiones. +5
"""
