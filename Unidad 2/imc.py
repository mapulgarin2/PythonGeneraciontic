peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso/(altura)**2

if imc < 18.5:
    resul = "bajo peso"
elif  imc > 18.5 and imc < 25 :
    resul = "normal" 
elif imc >= 25  and imc < 30 :
    resul = " sobrepeso" 
else:
    resul = "obesidad"
    
print(f"Para un peso de {peso} y una altura de {altura} su IMC es de {imc}, su estado es {resul}")    
    