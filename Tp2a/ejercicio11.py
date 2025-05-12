#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

#Respuesta: 

# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ").lower()

# Eliminar espacios y verificar si es palíndromo
palabra_sin_espacios = palabra.replace(" ", "")
if palabra_sin_espacios == palabra_sin_espacios[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")