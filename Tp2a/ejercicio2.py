#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Hemos asignado la lista x = [1,2,3] y ahora queremos asignar una copia a “y”. Podríamos hacer y = x[:], pero parece que y = x +[] 
# también funciona. ¿Es así?¿Por qué? 
#Respuesta:

#Se está sumando la lista x con una lista vacía ([]), el operador "+"" con listas devuelve una nueva lista, que contiene los elementos de ambas listas:
#x + [] crea una nueva lista con los mismos elementos que x.

# archivo: copiar_lista_simple.py

# Lista original
x = [1, 2, 3]

# Copia con slicing
y1 = x[:]

# Copia con suma de lista vacía
y2 = x + []

# Modificamos las copias para demostrar que son independientes
y1[0] = 100
y2[1] = 200

# Mostramos los resultados
print("Lista original x:", x)
print("Copia con x[:], y1:", y1)
print("Copia con x + [], y2:", y2)

