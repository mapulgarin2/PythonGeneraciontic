"""La búsqueda binaria es un algoritmo eficiente para buscar elementos en una
lista  ordenada.  Funciona  dividiendo  repetidamente  la  lista  a  la mitad
y descartando la mitad en la que no puede estar el valor buscado."""

def busqueda_binaria(lista,valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin :
        medio = (inicio + fin) // 2
        if lista[medio] == valor :
            return True
        elif lista[medio] > valor :
            fin = medio -1
        elif lista[medio] < valor :
            inicio = medio + 1
    return False

lista_1 = [15,23,67,78,97]    
print(busqueda_binaria(lista_1,100))    
                
            
            
            