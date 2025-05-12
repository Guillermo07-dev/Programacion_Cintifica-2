#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 

#Respuesta: 

# Diccionario con los precios de las frutas
precios_frutas = {
    'Manzana': 2.5,
    'Pera': 3.0,
    'Plátano': 1.8,
    'Uva': 4.0
}

# Preguntar al usuario por la fruta y los kilos
fruta = input("¿Qué fruta deseas comprar? (Manzana, Pera, Plátano, Uva): ").capitalize()
kilos = float(input("¿Cuántos kilos deseas comprar? "))

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    # Calcular el precio total
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total}€")
else:
    print(f"La fruta {fruta} no está disponible en la tienda.")
