"""Un diccionario en Python es una colección desordenada de pares clave-valor,
donde cada clave está asociada a un valor específico. A diferencia de  las  listas  y  las  tuplas,
los  diccionarios  no  están  ordenados,  lo  que significa  que  los  elementos  no  tienen  una  posición  definida.
Para acceder  a  los  valores  de  un  diccionario,  se  utilizan  las  claves correspondientes."""

#Crear un diccionario

mi_diccionario = {
    "Nombre":"Mauricio",
    "Edad" : "44",
    "Ciudad":"Pereira"
    }
print(mi_diccionario)
print(type(mi_diccionario))

#Acceder a los valores del diccionario

nombre = mi_diccionario["Nombre"]
edad = mi_diccionario["Edad"]
print(nombre)
print(edad)

#Modificar valor:

mi_diccionario["Ciudad"]="Dosquebradas"
print(mi_diccionario)

#Eliminar clave y cvalor
del mi_diccionario["Ciudad"]
print(mi_diccionario)

#Verificar si existe una clave en el diccionario
existe_ciudad = "Ciudad" in mi_diccionario
print(existe_ciudad)
existe_edad = "Edad" in mi_diccionario
print(existe_edad)

#Añadir una nueva clave-valor
mi_diccionario["Telefono"]= "3147520632"
print(mi_diccionario)

#Numeros de pares clave-valor en el diccionario
num_pares = len(mi_diccionario)
print(num_pares)



