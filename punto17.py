#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.  
#Respuesta:

# Constantes de conversión
PIE_A_CM = 30.48
PULGADA_A_CM = 2.54

# Solicita la distancia en pies
pies = float(input("Ingresa la distancia en pies: "))

# Solicita la distancia en pulgadas
pulgadas = float(input("Ingresa la distancia en pulgadas: "))

# Convierte la distancia total a centímetros
distancia_cm = (pies * PIE_A_CM) + (pulgadas * PULGADA_A_CM)

# Muestra el resultado
print(f"La distancia es {distancia_cm:.2f} centímetros.")
