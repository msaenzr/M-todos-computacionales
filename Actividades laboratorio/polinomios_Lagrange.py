from symtable import Symbol
from wsgiref import handlers
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import random as rd

#Ejemplo con tres puntos escogidos de la tabla A-4.

#Implementación con Numpy.
X = np.array([205,210,215])
Y = np.array([1274.3,1907.7,2105.9])
data = pd.read_csv("datos_actividad.csv",delimiter=";")

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

#Valores escogidos para realizar el análisis de todas las gráficas

tem_inter=[100, 138, 241, 145, 308, 94, 72, 87, 182]

# Análisis tabla Interpolación de P vs T

plt.plot(data['T'],data['Psat'],c='Violet')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de P vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Presión Saturada (KPa)")
plt.scatter(tem_inter,p_lagrange(data,tem_inter,'T','Psat'),c='Black')
plt.legend(["Original","Valores Intermedios"],loc="upper left")
plt.grid()
plt.show()

#Análisis tabla Interpolación de Sg vs T

plt.plot(data['T'],data['Sg'],c='Pink')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de Sg vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Entropía (kJ/kg*K)")
plt.scatter(tem_inter,p_lagrange(data,tem_inter,'T','Sg'),c='Black')
plt.legend(["Original","Valores Intermedios"],loc="upper left")
plt.grid()
plt.show()

#Análisis tabla Interpolación de Sf vs T

plt.plot(data['T'],data['Sf'],c='Blue')
plt.title("Tabla Interpolación de Sf vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Entropía (kJ/kg*K)")
plt.scatter(tem_inter,p_lagrange(data,tem_inter,'T','Sf'),c='Black')
plt.legend(["Original","Valores Intermedios"],loc="upper left")
plt.grid()
plt.show()

#Análisis de resultados y conclusiones

"""Como se puede observar en las gráficas, al evaluar puntos 


