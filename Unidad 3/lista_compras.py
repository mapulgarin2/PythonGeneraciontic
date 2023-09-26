def main():
    compras_lista = []
    
    while True:         
    
        print("\n Lista de Compras")
        print("1. Agregar un articulo")
        print("2. Eliminar un articulo")
        print("3. Ver lista de compras")
        print("4. salir")    
    
        option = input("Por favor seleccione una de las opciones: ")
    
        if option == "1":
            item = input("Ingrese el articulo: ")
            compras_lista.append(item)
        elif option == "2":
            item = input("Ingrese el articulo que desea eliminar: ")    
            if item in compras_lista:
                compras_lista.remove(item)
        elif option == "3":
            print("\n Tu lista de compras es: ")    
            for item in compras_lista:
                print(f"-{item}")
        elif option == "4":
            break
        else:
            print("Ingrese una opcion valida") 
            
if __name__== "__main__":
    main()
                       
    