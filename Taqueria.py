"""Uno de los mas populares para comer es la Taqueria de Poncho que ofrece un menu de platos principales
segun el diccionario a continuacion,donde el valor de cada clave es un precio en dolares:
{
    "Baja Taco" : 4.00,
    "Burrito" : 7.50,
    "Bowl" : 8.50,
    "Nachos" : 11.00,
    "Quesadillas" :  8.50,
    "Super Burrito" : 8.50,
    "Super Quesadilla" : 9.50,
    "Taco" : 3.00,
    "Tortilla Salad" : 8.00;    
}

En un archivo llamado Taqueria.py ,implemeta un programa que permita a un usuario realizar un pedido,
solicitandole articulos,uno por linea,hasta que el usuarioingresse CONTROL-D(Que es una forma comun de
finalizar la entrada de uno a un programa).Despues de cada articulo ingresado,muestre el costo total de todos 
los articulos ingredsados hasta ahora,con el prefijo de signo de dolar ($) y formateado con dos decimales.
trata la entrada del usuario sin distincion de mayusculas y minusculas .Ignora cualquier entrada que no 
sea un articulo. Suponga que cada articulo del menu estara en mayuscula."""  

def main():
    menu= {
        "Baja Taco" : 4.00,
        "Burrito" : 7.50,
        "Bowl" : 8.50,
        "Nachos" : 11.00,
        "Quesadillas" :  8.50,
        "Super Burrito" : 8.50,
        "Super Quesadilla" : 9.50,
        "Taco" : 3.00,
        "Tortilla Salad" : 8.00
}

while True:
    try:
        item = input("Ingrese un articulo de su pedido: ")
    except EOFError:
        break
    item=item.upper()
    
if item in menu:
    order_total = 0
    order_total += menu[item]
elif item == "CONTROL-D":
    print(f"El total de su pedido es ${order_total:.2f}")
    break
else:
    print("Articulo invalido") 
                
    
    
if  __name__=="__main__":
    main()
    

