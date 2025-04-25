#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto :  Pide al usuario ingresar un valor (número, texto, lista, etc.) y muestra su tipo de dato. 
#Respuesta

# Pedir al usuario que ingrese un valor
valor = input("Ingresa un valor (número, texto, lista, etc.): ")

# Mostrar el tipo de dato 
print("Tipo de dato antes de evaluar:", type(valor))

# Evaluar el valor para detectar su tipo 
try:
    valor_evaluado = eval(valor)
    print("Tipo de dato evaluado:", type(valor_evaluado))
except:
    print("No se pudo evaluar el valor. Se mantiene como string.")
