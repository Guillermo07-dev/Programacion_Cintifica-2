#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : ¿Que aparecerá por pantalla al evaluar la expresión [1] [0] ? ¿Y al evaluar la expresión [] [0]? 
#Respuesta:

#Evaluar [1][0]: Esto sí funciona. Se está creando una lista [1], y luego se accede al elemento con índice 0 de esa lista, el resultado mostrará [1].

#Evaluar [][0]: Esto lanza un error porque se está intentando acceder al índice 0 de una lista vacía ([]), lo cual no es posible.

# archivo: prueba_listas.py

# Caso 1: Lista con un elemento
try:
    resultado1 = [1][0]
    print("Resultado de [1][0]:", resultado1)
except Exception as e:
    print("Error en [1][0]:", e)

# Caso 2: Lista vacía
try:
    resultado2 = [][0]
    print("Resultado de [][0]:", resultado2)
except Exception as e:
    print("Error en [][0]:", e)
