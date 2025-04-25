#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto :  Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.
#Respuesta:

# Solicita la cantidad total de segundos
total_segundos = int(input("Ingresa una cantidad de segundos: "))

# Calcula horas, minutos y segundos
horas = total_segundos // 3600
minutos = total_segundos // 60
segundos_restantes = total_segundos % 60

# Muestra el resultado
print(f"{total_segundos} segundos son {horas} hora (s) {minutos} minuto(s) y {segundos_restantes} segundo(s).")