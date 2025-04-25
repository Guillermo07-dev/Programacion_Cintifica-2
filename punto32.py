#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto :  Convierte un carácter a su código ASCII (ord) y viceversa (chr). 
#Respuesta

# Pedir al usuario un carácter
caracter = input("Ingresa un carácter: ")
codigo_ascii = ord(caracter)

# Mostrar el código ASCII
print("Código ASCII de", caracter, "es:", codigo_ascii)

# Pedir al usuario un código ASCII
codigo = int(input("Ingresa un código ASCII: "))
caracter_resultante = chr(codigo)

# Mostrar el carácter correspondiente
print("Carácter correspondiente al código", codigo, "es:", caracter_resultante)
