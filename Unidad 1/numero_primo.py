numero = int(input("Ingrese un numero: "))

num_primo = True

if numero <= 1:
   num_primo = False
else:
    for i in range(2,(numero//2)+1):
        if numero%i == 0:
            print(i)
            num_primo = False
            break
        
if num_primo:
    print("EL numeo es primo")    
else:
    print("EL numero no es primo")        

# numero  =  int(input("Ingrese  un  número  entero 2positivo: "))
# es_primo = True
# if numero <= 1:
#     es_primo = False
# else:
#     for i in range(2, (numero // 2) + 1):
#         if numero % i == 0:
#             es_primo = False 
#             break
# if es_primo:
#     print("El número es primo.")
# else:
#     print("El número no es primo.")
