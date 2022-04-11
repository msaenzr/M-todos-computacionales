import numpy as np
from numpy.linalg import det, inv
from sympy import *

#Inversa de una matriz por librería Numpy
def inv_numpy(m_num):
    mf = inv(m_num)
    return mf

#Inversa de una matriz por librería Sympy
def inv_sympy(m_sim):
    mf = m_sim.inv()
    return mf

#Inversa de una matriz por método de la adjunta utilizando la librería Sympy
def inv_adjunta(m_sim,m,n):

    adj = m_sim.adjugate()
    d = m_sim.det()
    for i in range(0,m):
        for j in range(0,n):
            m_sim[i,j] = adj[i,j]/d
    return m_sim

#Función para recibir y retornar los datos.
def prom_inicio():

    m = int(input("Ingrese el número de filas: "))
    n = int(input("Ingrese el número de columnas: "))
    if n!=m:
        print("Los valores de la fila y de las columnas deben ser iguales, vuelva a ingresar.")
    else:
        print("Antes de insertar los valores de cada fila, asegurese de escribirlos\ncon un espacio intermedio, y sin espacio al comienzo y al final. Ejemplo: 1 2 3")
        m_num = np.zeros((m,n))
        m_sim = zeros(m,n)
        for i in range(0,n):
            fila = input(f'Inserte la fila #{i}: ')
            f = fila.split(' ')
            for j in range(0,len(f)):
                m_num[i][j]=f[j]
                m_sim[i,j]=f[j]
        print("La matriz insertada es: ")
        print (m_num)
        print("La matriz inversa por Numpy es: ")
        print(np.round(inv_numpy(m_num),3))
        print("La matriz inversa por Sympy es: ")
        print(inv_sympy(m_sim))
        print("La matriz inversa por el método de la adjunta es: ")
        print(inv_adjunta(m_sim,m,n))

#Llamar función principal
prom_inicio()