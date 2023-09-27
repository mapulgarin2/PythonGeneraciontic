
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
        
array_1 = [2,45,7,8,56,3,2,4,7,29,56,9]    
print(array_1)    

print(burble_sort(array_1))