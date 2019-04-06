# Crear un codigo que calcule las soluciones de la ecuacion cuadratica.

#axb2+bx+c = 0

#x1= -b + b2-4.a.c / 2a #primero el descriminante

#x2= -b-b2 -4.a.c/2a

#importar paquete  math

import math

a = float(input('favor ingresar a'))
b = float(input('favor ingresar b'))
c = float(input('favor ingresar c'))

discriminante = b ** 2 -4*a*c

if discriminante < 0:  #espacio normalmente se pide despues de dos puntos
    raiz = math.sqrt(-discriminante)* complex(0,1)  #por ser negativo
else:
    raiz = math.sqrt(discriminante)

x1 = (-b + raiz)/ (2*a)
x2 = (-b - raiz) / (2*a)

print (x1, x2)

#math.sqrt(2) #raiz cuadrada, la raiz del valor dentro del parentesis  2**2 doble asterisco. 100** 11

#depurar con la cuca,

#clic derecho evaluar expresiones

# alfanumericos , no se complique la vida, no caracter extrño, no tildes, lo mas simple posible



