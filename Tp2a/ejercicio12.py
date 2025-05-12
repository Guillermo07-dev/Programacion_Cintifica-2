#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Pedir al usuario que ingrese por teclado una lista de 3 elementos. 

#Respuesta: 

# Lista vacía
lista = []

# Pedir 3 elementos al usuario
print("Introduce 3 elementos para la lista:")
for i in range(3):
    elemento = input(f"Elemento {i + 1}: ")
    lista.append(elemento)

# Mostrar la lista
print("La lista ingresada es:", lista)
