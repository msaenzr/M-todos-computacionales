from this import d


X =[2,4,5,10,7,3,2,4]
Y = [34,45,67,21,34,45,33,90]

#Función para calcular la pendiente
def pendiente(X,Y):
    N = len(X)
    s_x = 0
    s_y = 0
    s_x2 = 0
    s_xy = 0
    for i in range(N):
        x_i = X[i]
        y_i = Y[i]
        s_x += x_i
        s_y += y_i
        s_x2 += (x_i)**2
        s_xy += (x_i*y_i)
    m = (N*s_xy - s_x*s_y)/(N*s_x2 - (s_x)**2)
    return m

#Función para calcular el punto de corte
def punto_c(X,Y):
    N = len(X)
    s_x = 0
    s_y = 0
    s_x2 = 0
    s_xy = 0
    for i in range(N):
        x_i = X[i]
        y_i = Y[i]
        s_x += x_i
        s_y += y_i
        s_x2 += (x_i)**2
        s_xy += (x_i*y_i)
    b = (s_x2*s_y - s_x*s_xy)/(N*s_x2 - (s_x)**2)
    return b

#Función para calcular la incertidumbre en general
def inc(X,Y):
    N =len(X)
    s=0
    for i in range(N):
        x_i =X[i]
        y_i = Y[i]
        m = pendiente(X,Y)
        b = punto_c(X,Y)
        s += (y_i - m*x_i - b)**2
    d = ((1/(N-2)) * s)**(1/2)
    return d

#Función para calcular la incertidumbre de la pendiente
def inc_m(X,Y,m,b):
    N = len(X)
    s_x =0
    s_x2 = 0
    for i in range(N):
        s_x += X[i]
        s_x2 += (X[i])**2
        d = inc(X,Y)
    d_m = d*((N)/(N*s_x2 - (s_x)**2))**(1/2)
    return d_m

#Función para calcular la incertidumbre del punto de corte
def inc_b():
    N = len(X)
    s_x =0
    s_x2 = 0
    for i in range(N):
        s_x += X[i]
        s_x2 += (X[i])**2
        d = inc(X,Y)
    d_b = d*((s_x2)/(N*s_x2 - (s_x)**2))**(1/2)   
    return d_b

#Función para calcular coeficiente de correlación
def coeficiente_c(X,Y):
    r = 0
    return r

print(pendiente(X,Y))