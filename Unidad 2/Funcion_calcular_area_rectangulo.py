import math


base = 2
#Parametros posiconales  se definen en el orden en que se esperanlos  valores  al  llamar  a  la  función  o  procedimiento. 
def calcular_area_rectangulo(altura,base):
     area = altura*base
     return area
     
area_rectangulo = calcular_area_rectangulo(5,3)
 
print(f"El area del rectangulo  es: {area_rectangulo}")

def saludar(nombre):
    print(f"Hola,{nombre} ")
    
    
saludar("Mauricio")#No es necesario llamar la funcion con print ,de esta manera el programa ya la interpreta por eso se llama una procedimiento y no devuelve un valor de retorno.

def saludar_1(nombre,saludo="Hola"):
    mensaje = saludo +" , "+ nombre
    print(mensaje)
    
# saludar_1("Alejandro","Hola")    
# saludar_1(nombre ="Alejandro",saludo="Hola")    
# saludar_1("Alejandro","En la buena !")    
saludar_1("Alejandro")    

def area_Circulo(radio):
    area = (math.pi)*radio
    return area