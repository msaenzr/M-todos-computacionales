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

#Algoritmo para obtener n datos aleatorios entre los rangos escogidos para cada interpolación.

def datos_intermedios(data,min,max,key_1,key_2,n):
    l_x=[]
    l_y=[]
    for n in range(n):
        x = rd.randint(min,max)
        y = p_lagrange(data,x,key_1,key_2)
        if y>0:
            l_x.append(x)
            l_y.append(y)
    return (l_x,l_y)

# Análisis tabla Interpolación de P vs T

#dat = datos_intermedios(data,0,373,'T','Psat',50)
#print(dat)
plt.plot(data['T'],data['Psat'],c='Violet')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de P vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Presión Saturada (KPa)")
plt.show()

#plt.plot(dat[0],dat[1],c='Black')
#plt.show()

#Análisis tabla Interpolación de Sg vs T
plt.plot(data['T'],data['Sg'],c='Pink')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de Sg vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Entropía (kJ/kg*K)")
plt.show()

#Análisis tabla Interpolación de Sf vs T
plt.plot(data['T'],data['Sf'],c='Blue')
plt.legend(["Original"],loc="upper left")
plt.title("Tabla Interpolación de Sf vs T")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Entropía (kJ/kg*K)")
plt.show()


"""
Gráficas en formato png.  Los ejes deben aparecer debidamente identificados y el tamaño de las etiquetas debe ser visible. +10
Análisis de resultados y conclusiones. +5
"""
