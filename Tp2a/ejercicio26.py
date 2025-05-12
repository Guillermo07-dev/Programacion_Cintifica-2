#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. 

#Respuesta: 

# Crear un diccionario para almacenar los datos del usuario
usuario = {}

# Pedir los datos al usuario
usuario['nombre'] = input("¿Cuál es tu nombre? ")
usuario['edad'] = input("¿Cuántos años tienes? ")
usuario['direccion'] = input("¿Dónde vives? ")
usuario['telefono'] = input("¿Cuál es tu número de teléfono? ")

# Mostrar el mensaje con los datos del diccionario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
