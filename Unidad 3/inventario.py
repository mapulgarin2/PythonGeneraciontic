inventario = {"Manzana":10,
              "Mango": 4,
              "Banano": 7}
print(inventario)

def gestion_inventario(accion,articulo,cantidad = 0):
    if accion == "Agregar":
        if articulo in inventario:
            inventario[articulo] += cantidad
        else :
            inventario[articulo] = cantidad
    elif   accion == "Quitar" :
        if articulo in inventario and inventario[articulo] >= cantidad:
            inventario[articulo]-=cantidad
        else:
            print("No se puede realizar la acción")    
    elif accion == "Buscar" :
        if articulo in inventario:
            return inventario[articulo]
        else:
            return None
    else:
        print("Accion no reconocida")
            
    
gestion_inventario("Agregar","Manzana",5)  
print(inventario)  
    
gestion_inventario("Quitar","Mango",4)  
print(inventario)  
    
 
print(gestion_inventario("Buscar","Banano") )      
        
        
            
            
        
           
        
        
        
    
