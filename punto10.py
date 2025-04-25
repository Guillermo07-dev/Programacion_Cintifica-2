#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Pide dos números y una operación (+, -, *, /), luego muestra el resultado. 
#Respuesta:

numero1 = float(input("ingresa un numero:"))
numero1 = int(numero1)
numero2 = float(input("ingresa otro numero"))
numero2 = int(numero2)

operacion = input("Ingresa una operación (+, -, *, /): ")

if operacion == '+':
    resultado = numero1 + numero2
elif operacion == '-':
    resultado = numero1 - numero2
elif operacion == '*':
    resultado = numero1 * numero2
elif operacion == '/':
    # Verifica que no haya división por cero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: División por cero, operación no válida"

# Muestra el resultado
print(f"Resultado: {resultado}")