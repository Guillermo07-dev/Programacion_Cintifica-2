#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Piensa que quieres usar un diccionario para organizarte. Diseña una agenda donde 
#quieres anotar las tareas. Para ello, pedirás al usuario lo siguiente: 'Dime el día de la 
#semana...' Usuario: lunes. 'Tienes 0 tareas pendientes. ¿Qué anotamos?'. Si hubiera 
#alguna tarea, se mostraría cada elemento. Como ves, la clave será el día y el valor de una lista.  
 
#Respuesta: 

# Crear el diccionario para la agenda
agenda = {
    'lunes': [],
    'martes': [],
    'miércoles': [],
    'jueves': [],
    'viernes': [],
    'sábado': [],
    'domingo': []
}

# Función para mostrar las tareas de un día
def mostrar_tareas(dia):
    if len(agenda[dia]) == 0:
        print(f"Tienes 0 tareas pendientes para el {dia}. ¿Qué anotamos?")
    else:
        print(f"Tareas pendientes para el {dia}:")
        for tarea in agenda[dia]:
            print(f"- {tarea}")

# Función para añadir tareas
def anotar_tarea(dia):
    tarea = input(f"Introduce una tarea para el {dia}: ")
    agenda[dia].append(tarea)
    print(f"Tarea '{tarea}' añadida para el {dia}.")

# Función principal
def agenda_principal():
    while True:
        dia = input("Dime el día de la semana (o 'salir' para terminar): ").lower()
        if dia == 'salir':
            print("Gracias por usar la agenda. ¡Hasta pronto!")
            break
        if dia in agenda:
            mostrar_tareas(dia)
            if len(agenda[dia]) == 0 or input("¿Quieres añadir una tarea? (sí/no): ").lower() == 'sí':
                anotar_tarea(dia)
        else:
            print("Día inválido, por favor ingresa un día de la semana válido.")

# Llamada a la función principal para iniciar la agenda
agenda_principal()
