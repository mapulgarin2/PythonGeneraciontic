def funcion_recursiva(n):#uncion factorial
    #caso base
    if n == 0:
        return 1
    #caso recursiva
    else :
        return n*funcion_recursiva(n - 1) 
    
#Caso de estudio 

resultado = funcion_recursiva(4)    
print(resultado)

def suma_naturales(m):
    if m == 0 :
        return 0
    else:
        return m + suma_naturales(m - 1)
    
resultado = suma_naturales(5)    
print(resultado)

#___________________________________________________________________________