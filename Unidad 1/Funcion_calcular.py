import math

def calcular_area_cuadrado(lado):
    return lado*lado

def calcular_area_circulo(radio):
    return math.pi* (radio**2)

#Uso lado de las funciones
Lado_cuadrado = 5
radio_circulo = 3

area_caudrado = calcular_area_cuadrado(Lado_cuadrado)
area_circulo = calcular_area_circulo(radio_circulo)

print("El area del cuadrado es: "+ str(area_caudrado))
print(f"El area del circulo es: {round(area_circulo,2)}")
