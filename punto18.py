#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Escriba un programa que pida una distancia en pulgadas y que escriba esa distancia en centímetros.  
#Se recuerda que una pulgada son 2,54 cm.
#Respuesta:

# Constantes de conversión
PULGADA_A_CM = 2.54

# Solicita la distancia en pulgadas
pulgadas = float(input("Ingresa la distancia en pulgadas: "))

# Convierte la distancia total a centímetros
distancia_cm =  (pulgadas * PULGADA_A_CM)

# Muestra el resultado
print(f"La distancia es {distancia_cm:.2f} centímetros.")