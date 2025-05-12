#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.  

#Respuesta:

# Crear la lista con los números del 1 al 10
numeros = list(range(1, 11))

# Invertir la lista
numeros_invertidos = numeros[::-1]

# Mostrar los números separados por comas
print("Números del 10 al 1:")
print(", ".join(str(num) for num in numeros_invertidos))
