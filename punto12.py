#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto : Escribí un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde. 
#Respuesta:

Horas_trabajadas = input("¿Cuantas horas has trabajado?: ")
Horas_trabajadas = int(Horas_trabajadas)

Coste_Hora = input("¿Cuánto cuesta la hora de trabajo?: ")
Coste_Hora = int(Coste_Hora)

Paga = (Horas_trabajadas * Coste_Hora)
print(f"Tu paga correspondiente es de:$",Paga)
