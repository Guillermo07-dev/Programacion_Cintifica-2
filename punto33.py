#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto :  Pide al usuario ingresar una expresión matemática simple (ej: 2 + 3 * 5) y evalúala. 
#Respuesta

# Pedir al usuario una expresión matemática
expresion = input("Ingresa una expresión matemática: ")

# Evaluar la expresión
try:
    resultado = eval(expresion)
    print("Resultado:", resultado)
except Exception as e:
    print("Error al evaluar la expresión:", e)
