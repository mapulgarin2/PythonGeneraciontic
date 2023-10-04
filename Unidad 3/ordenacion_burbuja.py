import random
def burble_sort(array):
    largo = len(array) - 1
    #Bucle para las pasadas
    for i in range(0,largo):
        #bucle para comparaciones e intercambios
        for j in range(0,largo):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j]= array[j+1]
                array[j +1]= aux
    return array        
        
# array_1 = [2,45,7,8,56,3,2,4,7,29,56,9]    
# print(array_1)    

# print(burble_sort(array_1))

#________________busqueda lineal___________________________

# def linear_search(lista,elemento):
#     for i in range(len(lista)):
#         if lista[i] == elemento:
#             return i
#     return -1

# numeros = [2,5,7,9,45,1,90, 0]
# elemento_busacado = 3
# indice = linear_search(numeros,elemento_busacado)

# if indice != -1 :
#     print(f"El elemento busacado {elemento_busacado} se encuentra en la lista {numeros}")
# else :
#     print(f"El elemento busacado {elemento_busacado} no se encuentra en la lista {numeros}")    

numeros = [random.randint(1,100) for _ in range(20)]
print(numeros)

lista_ordenada = burble_sort(numeros)
print(lista_ordenada)