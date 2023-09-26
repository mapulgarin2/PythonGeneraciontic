"""Un  conjunto  en  Python  es  una  colección  desordenada  de  elementos únicos.
A diferencia de las listas y las tuplas, los conjuntos no permiten elementos duplicados 
y no tienen un orden definido.
Los conjuntos son útiles cuando necesitamos almacenar elementos sin importar su ordeno  cuando
necesitamos  realizar  operaciones  como  intersecciones,uniones y diferencias entre conjuntos."""

#Crear conjuto
mi_conjunto = {1,2,3,4,5,5,5,6,7,8,8,9,10}
print(mi_conjunto)

#Adiccionar un elemento a un conjunto
mi_conjunto.add(12)
print(mi_conjunto)

mi_conjunto_1 = {1,5,3,7,2,2,9,8,8,10}
print(mi_conjunto_1)

#Eliminar un elemento a un cojunto
mi_conjunto_1.remove(3)
print(mi_conjunto_1)

#verificar si un elemto esta en el conjunto

existe = 4 in mi_conjunto
print(existe)
existe_1 = 4 in mi_conjunto_1
print(existe_1)

#Numero de elementos 
cant = len(mi_conjunto)
print(cant)
cant_1 = len(mi_conjunto_1)
print(cant_1)
