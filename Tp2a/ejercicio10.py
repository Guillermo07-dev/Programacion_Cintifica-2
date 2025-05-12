#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : Convierte la lista a=[1,[2,[3,4]],5] en [1,[2,[3, 4],[6,7]], 5].  

#Respuesta:

a = [1, [2, [3, 4]], 5]

# Insertar [6, 7] en el nivel adecuado
a[1].append([6, 7])

print(a)
