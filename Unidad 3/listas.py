"""Una lista en Python es una colección ordenada de elementos separados
por  comas  y  encerrados  entre  corchetes.  Cada  elemento  de  una  lista
puede ser de cualquier tipo de datos válido, como números, cadenas detexto,
booleanos e incluso otras listas. 
La principal característica de las listas  es  que  son  mutables,
lo  que  significa  que  se  pueden  modificar después de su creación"""

#Crear una lista
mi_lista = [1,2,3,4,5]
print(mi_lista)

#mostrar elemento de una lista

elemento = mi_lista[0]
print(elemento)

#modificar elemento de una lista
mi_lista[0]=10
print(mi_lista)

#Eliminar un elemento de la lista
del mi_lista[0]
print(mi_lista)


#Adicionar un elemento en la ultima posicion
mi_lista.append(9)
print(mi_lista)


#Concocer la longuitud de una lista
Largo_lista = len(mi_lista)
print(Largo_lista)