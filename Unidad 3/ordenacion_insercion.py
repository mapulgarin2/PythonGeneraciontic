def ordenacion_insercion(array):
    length = len(array)
    
    for i in range(1,length):
        insert_value = array[i]
        insert_index = i
        
        while insert_index > 0  and  array[insert_index - 1] > insert_value :
            array[insert_index] = array[insert_index - 1]
            insert_index -= 1
        array[insert_index] = insert_value
    
    return array    


# def ordenacion_insercion(array):
#     n = len(array)
#     for i in range(1,n):
#         valor_actual = array[i]
#         j = i -1 
#         while j >= 0 and array[j] > valor_actual :
#             array[j +1] = array[j]
#             j -= 1
#         array[j + 1] = valor_actual
#     return array
            
            
lista = [4, 2, 6, 1, 8, 3]
print(ordenacion_insercion(lista))
