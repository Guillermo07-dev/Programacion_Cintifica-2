#Stevens Guillermo
#2025
#Programacion Cientifica TP2a
#Contenido del punto : ¿Sabrías decir qué resultados se mostrarán al ejecutar estas sentencias? 

#a. >>> [1, 2, 3] < [1, 2]  False 
#b. >>> [1, 1] < [1, 2]  
#c. >>> [1, 3] < [1, 2]  
#d. >>> [10, 20, 30] > [1, 2, 3] 
#e. >>> [10, 20, 3] > [1, 2, 3]  
#f. >>> [10, 2, 3] > [1, 2, 3]  
#g. >>> [1, 20, 30] > [1, 2, 3]  
#h. >>> [0, 2, 3] <= [1, 2, 3]  
#i. >>> [1] < [2, 3]  
#j. >>> [1] < [1, 2]  
#k. >>> [1, 2] < [0]  

#Respuesta:

#a. Resultado: False. Porque [1, 2, 3] es más larga y los elementos hasta la longitud de la más corta ([1, 2]) son iguales. 
# Así que la lista más larga se considera mayor.

#b.  [1, 1] < [1, 2]. Resultado: True.  El primer elemento es igual, pero 1 < 2 en la segunda posición.

#c. Resultado: False. El primer elemento es igual, pero 3 > 2 en la segunda posición.

#d. Resultado: True. 10 > 1 en la primera posición.

#e. Resultado: True. 10 > 1 en la primera posición.

#f. Resultado: True. 10 > 1 en la primera posición.

#g.  Resultado: True. El primer elemento es igual, pero 20 > 2 en la segunda posición.

#h. Resultado: True. 0 < 1 en la primera posición.

#i. Resultado: True. 1 < 2 en la primera posición.

#j.  Resultado: True. Primeros elementos iguales, pero la primera lista es más corta, entonces se considera menor.

#k. Resultado: False. 1 > 0 en la primera posición.

# archivo: comparaciones_listas.py

print("a.", [1, 2, 3] < [1, 2])         # False
print("b.", [1, 1] < [1, 2])            # True
print("c.", [1, 3] < [1, 2])            # False
print("d.", [10, 20, 30] > [1, 2, 3])   # True
print("e.", [10, 20, 3] > [1, 2, 3])    # True
print("f.", [10, 2, 3] > [1, 2, 3])     # True
print("g.", [1, 20, 30] > [1, 2, 3])    # True
print("h.", [0, 2, 3] <= [1, 2, 3])     # True
print("i.", [1] < [2, 3])               # True
print("j.", [1] < [1, 2])               # True
print("k.", [1, 2] < [0])               # False

