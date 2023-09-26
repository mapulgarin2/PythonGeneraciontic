"""La búsqueda lineal es un enfoque simple pero efectivo para buscar un elemento  en  una
lista.Consiste  en  recorrer  la  lista  elemento  por elemento hasta encontrar el valor
buscado."""
def busqueda_lineal(lista_1,valor):
    for elemento in lista_1:
        if elemento == valor:
            return True
    return False

lista_1 = [1,2,3,4,5]    

print(busqueda_lineal(lista_1,4))