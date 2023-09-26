#Estructura basica para definir una clase
# class Persona:
#     def __init__(self,nombre,edad) -> None:#El metodo constructor
#         self.nombre = nombre
#         self.edad = edad
        
#     def saludar(self):
#         print(f"Hola mi nombre es {self.nombre}")
        
#     def obtener_Edad(self)    :
#         return self.edad
    
# persona = Persona("Mauricio",23)

# print(persona.nombre)#Imprime el nombre

# persona.saludar()#Imprime "Hola mi nombre es Mauricio"

# edad = persona.obtener_Edad()#Imprime la edad
# print(edad)

#___________________________________________________________________________________

class Producto :
    def __init__(self,nombre,precio) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def mostrar_informacion(self)    :
        print(f"El nombre es: {self.nombre} y el valor es: ${self.precio} pesos")
        # print(f"El valor es: ${self.precio} pesos")
        
producto =Producto("Camisa",23.45)
producto_1 =Producto("Pantalon",20)

producto.mostrar_informacion()
producto_1.mostrar_informacion()

# print(producto.mostrar_informacion()) No es necesario llamar print por que la funcion es para imprimir.
# print(producto_1.mostrar_informacion())

#_________________________________________________________________________________
#Herencia de clases

class Animal:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        
    def saludar(self):
        print(" !Hola ¡ Soy un animal¡")
        
class Perro(Animal):
    def ladrar(self):
        print("!Guau¡")
        
perro = Perro("Fido")     

print(perro.nombre)

perro.saludar()

perro.ladrar()

#________________________________________________________________________________________________________-
"""El  polimorfismo  es  la  capacidad  de  un  objeto  de  tomar  diferentes formas
o  comportarse de  diferentes  maneras  según  el  contexto.
En Python,  el  polimorfismo  se  logra  a  travésde  la  sobreescritura  demétodos."""

class Animal:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        
    def saludar(self)    :
        print(f"Hola Soy un Animal y mi nombre es {self.nombre}")
        
class Perro(Animal)        :
    def saludar(self):
        print(f"Guau soy un perro y me llamo {self.nombre}")
        
class Gato(Animal)        :
    def saludar(self):
        print(f"Miau soy un gato y me llamo {self.nombre}")
animal= Animal("Pepe")       
animal_1 = Perro("Gary")
animal_2 = Gato("Misifu")

print(animal.nombre)
print(animal_1.nombre)
print(animal_2.nombre)

animal.saludar()
animal_1.saludar()
animal_1.saludar()