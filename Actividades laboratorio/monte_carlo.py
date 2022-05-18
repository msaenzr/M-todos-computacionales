import numpy as np
import random as rd
from matplotlib import pyplot as plt

#Datos necesarios del problema a resolver
R= 8.31446261815324 #Constante de los gases
T = 300 #Temperatura
M= 0.016 #Masa molar del oxígeno
A = (M/2*np.pi*R*T)**(3/2)

#Función para generar un número aleatorio
def num_ale(min,max):
    #min: Límite inferior de integración
    #máx: Límita superior de integración
    ch = rd.uniform(min,max)
    return ch
#Comprobación de la función para generar un número aleatorio e impresión de expresión matemática
num_ale(1,3)
print(f"Valor de expresión matemática hallada (np.log(100)/(np.log(2))+1): {np.log(100)/(np.log(2))+1}")

#Generación de gráfica de prueba (Histograma)
a =2
b = 5
x = [num_ale(a,b) for i in range(100)]
plt.hist(x,bins=15, density =True)
plt.title("Gráfica de prueba")
plt.xlabel("Números aleatorios")
plt.savefig("Prueba.png")

#Definición de Función de distribución de velocidades de Maxwell (Se agrega un factor cuadrático de la velocidad)
def f(v):
    return 4*np.pi*A*(v**2)*np.exp(-M*v**2/(2*R*T))

#Definición de método de integral Monte Carlo
def integral_montecarlo(n):
    #n:Número de muestras
    c_inf = 0  #c_inf: Cota inferior
    c_sup = 10000 #c_sup:Cota superior
    suma_n = 0 #suma_n: Suma de las muestras
    for i in range(n):
        r = num_ale(c_inf, c_sup)
        suma_n += f(r)
    promedio = float(suma_n/n)
    return (c_sup-c_inf)*promedio

#Impresión de resultados (Integral y velocidad rms para el oxígeno)
n = 1000
int_mc = integral_montecarlo(n)
print (f"\nEl valor de la integral es: {int_mc}")
v_rms = np.sqrt(int_mc)
print(f"\nLa velocidad del oxígeno en forma monoaómica es: {v_rms} m/s")

#Generación de datos para gráfica de muestreo
list_int =[]
rango_muestreo = range(1,10000,200)
for n in rango_muestreo:
    list_int.append(integral_montecarlo(n))

#Gráfica de muestreos
plt.figure()
plt.scatter(rango_muestreo,list_int)
plt.xlabel("Datos Muestreo (n)")
plt.ylabel("<F(v)>")
plt.title("<F(v)> vs Datos Muestreo")
plt.savefig("Figura.png")
plt.show()

#Análisis de los resultados 
print("\nAnálisis de resultados: \n")
print("En primer lugar, el análisis para la gráfica de prueba no se tendrá \
en cuenta debido que como lo menciona su nombre, es de prueba. Ahora \
 bien, para la ultima gráfica presentada '<F(v)> vs Datos Muestreo' se evidencia \
una gran dispersión en los datos, debido a los números aleatorios generados \
por la libreria Random. Aún así, se logra obtener la velocidad rms del oxígeno \
el cual posee un gran valor teniendo en cuenta el factor cuadrático de la velocidad\
que no fue agregado en clase. En ese sentido, se obtiene un valor alto para \
la velocidad. ")