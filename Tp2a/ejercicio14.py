#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : La lista del punto 9 convertir en una tupla. 

#Respuesta: 

# Crear una lista del 1 al 10
lista = list(range(1, 11))

# Convertir la lista en una tupla
tupla = tuple(lista)

# Invertir la tupla
tupla_invertida = tupla[::-1]

# Mostrar la tupla en orden inverso, separada por comas
print(", ".join(str(num) for num in tupla_invertida))
