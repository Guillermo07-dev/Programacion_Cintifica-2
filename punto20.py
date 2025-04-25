#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit. 
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32  
#Respuesta:

# Solicita la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convierte a grados Fahrenheit
fahrenheit = 1.8 * celsius + 32

# Muestra el resultado
print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F.")