#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (IMC), con un decimal. 
#Se recuerda que el imc se calcula con la fórmula imc = peso / (altura**2) 
#Respuesta:

# Solicita el peso en kilogramos
peso = float(input("Ingresa tu peso en kilogramos: "))

# Solicita la altura en metros
altura = float(input("Ingresa tu altura en metros: "))

# Calcula el IMC
imc = peso / (altura ** 2)

# Muestra el resultado
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")