"""A diferencia de las listas, las tuplas son estructuras de datos inmutables en Python.
Esto significa que una vez creada una tupla, no se pueden modificar sus elementos.
Las tuplas se crean separando los elementos por comas y encerrándolos entre paréntesis."""

#Crear una tupla
mi_tupla = (1,2,3,4,5)

#Acceder a un elemento de una tupla
primer_elemento = mi_tupla[0]
segundo_elemento = mi_tupla[3]
print(primer_elemento)
print(segundo_elemento)

#No se puede modificar una tupl existente
#mi_tupla[0]= 2 --->esto genera un error 

longuitud_tupla= len(mi_tupla)
print(longuitud_tupla)

