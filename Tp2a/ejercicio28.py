#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Construye un sistema escolar entero para el IPET 1308 de 25 de Mayo. Para ello, el 
#diccionario principal contendrá las carreras con la información de precio y nombre. Dentro de estas, existirán nuevos diccionarios para almacenar la siguiente 
#información: ‘profesor, contacto, lista de alumnos totales, evaluación promedio‘. 

#Respuesta: 

# Diccionario principal con carreras
carreras = {
    "Ingeniería en Sistemas": {
        "precio": 5000,
        "nombre": "Ingeniería en Sistemas",
        "profesor": "Dr. Juan Pérez",
        "contacto": "juan.perez@ipet1308.edu",
        "alumnos_totales": ["Carlos Martínez", "Ana López", "Pedro Gómez", "Lucía Ramírez"],
        "evaluacion_promedio": 8.5
    },
    "Analista de Sistemas": {
        "precio": 4000,
        "nombre": "Analista de Sistemas",
        "profesor": "Ing. María González",
        "contacto": "maria.gonzalez@ipet1308.edu",
        "alumnos_totales": ["Jorge Ruiz", "Beatriz Castro", "Daniel Fernández", "Clara González"],
        "evaluacion_promedio": 7.3
    },
    "Técnico en Informática": {
        "precio": 3500,
        "nombre": "Técnico en Informática",
        "profesor": "Lic. Luis García",
        "contacto": "luis.garcia@ipet1308.edu",
        "alumnos_totales": ["Ricardo Pérez", "Sofía Rodríguez", "Martín Díaz", "Elena Torres"],
        "evaluacion_promedio": 8.0
    }
}

# Función para mostrar información de una carrera
def mostrar_info_carrera(carrera):
    if carrera in carreras:
        info = carreras[carrera]
        print(f"Carrera: {info['nombre']}")
        print(f"Precio: ${info['precio']}")
        print(f"Profesor: {info['profesor']}")
        print(f"Contacto: {info['contacto']}")
        print(f"Alumnos: {', '.join(info['alumnos_totales'])}")
        print(f"Evaluación promedio: {info['evaluacion_promedio']}")
    else:
        print("Carrera no encontrada.")

# Función para agregar un alumno a una carrera
def agregar_alumno(carrera, alumno):
    if carrera in carreras:
        carreras[carrera]['alumnos_totales'].append(alumno)
        print(f"{alumno} ha sido añadido a la carrera {carrera}.")
    else:
        print("Carrera no encontrada.")

# Función para actualizar la evaluación promedio de una carrera
def actualizar_evaluacion(carrera, nueva_evaluacion):
    if carrera in carreras:
        carreras[carrera]['evaluacion_promedio'] = nueva_evaluacion
        print(f"La evaluación promedio de la carrera {carrera} ha sido actualizada a {nueva_evaluacion}.")
    else:
        print("Carrera no encontrada.")

# Menú de opciones para interactuar con el sistema
def menu():
    while True:
        print("\n--- Sistema Escolar IPET 1308 ---")
        print("1. Ver información de una carrera")
        print("2. Agregar alumno a una carrera")
        print("3. Actualizar evaluación promedio de una carrera")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            carrera = input("Ingrese el nombre de la carrera: ")
            mostrar_info_carrera(carrera)
        elif opcion == '2':
            carrera = input("Ingrese el nombre de la carrera: ")
            alumno = input("Ingrese el nombre del alumno: ")
            agregar_alumno(carrera, alumno)
        elif opcion == '3':
            carrera = input("Ingrese el nombre de la carrera: ")
            nueva_evaluacion = float(input("Ingrese la nueva evaluación promedio: "))
            actualizar_evaluacion(carrera, nueva_evaluacion)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar el menú
menu()
