#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Pide la hora actual (formato 24h) e imprime: 
#"Buenos días" si es antes de las 12. 
#"Buenas tardes" si es entre las 12 y 18. 
#"Buenas noches" si es después de las 18.
#Respuesta:

# Solicita la hora actual al usuario
hora = int(input("Ingresa la hora actual (formato 24h, solo número): "))

# Verifica y muestra el saludo adecuado
if 0 <= hora < 12:
    print("¡Buenos días!")
elif 12 <= hora < 18:
    print("¡Buenas tardes!")
elif 18 <= hora < 24:
    print("¡Buenas noches!")
else:
    print("Hora no válida. Debe estar entre 0 y 23.")
