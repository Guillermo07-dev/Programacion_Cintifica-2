#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : La tupla dada es una tupla anidada. Escribe un programa Python para imprimir el valor 20. tuple1 = ("Orange", [10, 20, 30], (5, 15, 25)) 

#Respuesta: 

# Tupla anidada
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# Acceder al valor 20
valor = tuple1[1][1]  # tuple1[1] accede a la lista, y [1] a la posición 20

# Imprimir el valor 20
print("El valor 20 es:", valor)
