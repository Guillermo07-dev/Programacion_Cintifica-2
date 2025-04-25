#Stevens Guillermo
#2025
#Programacion Cientifica TP1b
#Contenido del punto :  Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son. 
# Se recuerda que una gruesa son doce docenas. 
#Respuesta:

# Solicita la cantidad total de unidades
cantidad = int(input("Ingresa una cantidad de unidades: "))

# Calcula cuántas gruesas hay
gruesas = cantidad // 144

# Calcula las unidades restantes después de contar las gruesas
resto_despues_gruesas = cantidad % 144

# Calcula las docenas dentro del resto
docenas = resto_despues_gruesas // 12

# Calcula las unidades restantes
unidades = resto_despues_gruesas % 12

# Muestra el resultado
print(f"{cantidad} unidades son:")
print(f"{gruesas} gruesa(s)")
print(f"{docenas} docena(s)")
print(f"{unidades} unidad(es)")
