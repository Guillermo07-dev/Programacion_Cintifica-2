#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista 
# y los muestre por pantalla ordenados de menor a mayor. 

#Respuesta:

# Pedir al usuario que introduzca los números ganadores
numeros = []

print("Introduce los 6 números ganadores de la Lotería Primitiva (entre 1 y 49):")
while len(numeros) < 6:
    try:
        num = int(input(f"Introduce el número {len(numeros) + 1}: "))
        if num < 1 or num > 49:
            print("El número debe estar entre 1 y 49.")
        elif num in numeros:
            print("Este número ya fue introducido.")
        else:
            numeros.append(num)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Ordenar la lista
numeros.sort()

# Mostrar los números ordenados
print("Números ganadores ordenados de menor a mayor:")
print(numeros)

