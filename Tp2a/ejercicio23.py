#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Pide al usuario que impute una lista de alumnos, separados con “;”. Después, pregunta por las notas de ellos. 
# Realizar diccionario para después poder preguntar a alguien y observar su nota. 
 
#Respuesta: 

# Pedir al usuario que ingrese los nombres de los alumnos separados por punto y coma
alumnos = input("Introduce los nombres de los alumnos, separados por ';': ").split(';')

# Crear un diccionario para almacenar las notas
notas = {}

# Preguntar por las notas de cada alumno
for alumno in alumnos:
    alumno = alumno.strip()  # Eliminar espacios extra al principio y al final
    nota = input(f"Introduce la nota de {alumno}: ")
    notas[alumno] = nota

# Consultar por un alumno y mostrar su nota
consulta = input("Introduce el nombre del alumno para consultar su nota: ").strip()

if consulta in notas:
    print(f"La nota de {consulta} es: {notas[consulta]}")
else:
    print("El alumno no se encuentra en la lista.")
