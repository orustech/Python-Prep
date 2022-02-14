# 1) Tarea de clase 1 Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

from os import supports_bytes_environ


mi_var = 2
print(mi_var)

# 2) Imprimir el tipo de dato de la constante 8.5

mi_var2 = 8.5
print(type(mi_var2))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(mi_var))


# 4) Crear una variable que contenga tu nombre

nombre = 'David'
print (nombre)

# 5) Crear una variable que contenga un número complejo

complex = 2 + 3j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complex))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

PI = 3.14159
print (round(PI, 4))

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

VAR1 = 'true'
var2 = True 

print (VAR1, var2)

#  9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print(type(VAR1))
print(type(var2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

Sum = (mi_var + PI)  
print (Sum)

# 11) Realizar una operación de suma de números complejos
complex2 = 2 + 1j
SUM2 = complex + complex2
print (SUM2)

# 12) Realizar una operación de suma de un número real y otro complejo

Sum3 = mi_var + complex
print (Sum3)

# 13) Realizar una operación de multiplicación

Product = mi_var * complex
print (Product)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print (mi_var ** 8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

Div= 27/4
print(Div)
# 16) de la división anterior solamente mostrar la parte entera

print (int(Div))

# 17)  De la división de 27 entre 4 mostrar solamente el resto

divr= 27 % 4
print (divr)  


# 18)  Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print (int(Div)*4 + divr)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
alf1= 'Volde@'
alf2 = 'mort@'

print (alf1 + alf2)


# 20 ) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a= 2
b = '2'

print(a==b) 

#Esto ocurre porque los elementos comparados son de diferente grupo, ya que uno pertenece a los enteros, mientras que el otro al str

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print (a == int(b))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

c  = float('3.8') 
print (c)

# el error se presenta porque la variable float debe estar determinado por un punto y esta escrito con una coma.

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

d = 3
d -= 5
print (d)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print (1 << 2 )