#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Imagina partir de una super lista de notas en formato texto, algo parecido a esto: 
#‘7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;‘. ¿Serías capaz de extraer el patrón para 
#construir un diccionario donde la clave son los nombres y el valor de la puntuación promedio? 

#Respuesta: 

# Cadena con las notas de los alumnos
super_lista = '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'

# Crear un diccionario para almacenar los resultados
diccionario_notas = {}

# Dividir la cadena por el separador ';;' para separar cada persona
personas = super_lista.split(';;')

# Recorrer la lista de personas
for persona in personas:
    if persona:  # Evitar procesar una cadena vacía
        # Dividir la persona por el separador '#'
        notas_y_nombre = persona.split('#')
        
        # Obtener las notas y el nombre
        notas = list(map(float, notas_y_nombre[0].split(',')))  # Convertir las notas a flotantes
        nombre = notas_y_nombre[1]
        
        # Calcular el promedio de las notas
        promedio = sum(notas) / len(notas)
        
        # Almacenar el resultado en el diccionario
        diccionario_notas[nombre] = promedio

# Mostrar el diccionario con los nombres y sus promedios
print(diccionario_notas)
