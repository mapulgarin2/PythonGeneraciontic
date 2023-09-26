precio = 50
adeudado = precio
ingresado = 0
valor = [25,10,5]

while adeudado > 0:
    monto = int(input("Ingrese una modeda (de 5 ,10 o 25 centavos): "))
    if monto in valor:
        ingresado += monto
        adeudado -= monto
        print(f"El monto adeudado es: {adeudado} centavos")
    else:
        print(" La moneda no corresponde al valor requerido")    
        
if ingresado > precio:
    cambio = ingresado - precio
    print(f"El cambio es: {cambio}centavos ")        
    