notas = []#Vuelvo la notas una libreria

while True :#Valido qu emientras que todo sea verdad realizar la siguiente accion o acciones
    nota = input("Ingrese la nota(Digite 'salir' si no va ha ingresar mas notas): ")
    if nota.lower()=="salir":
        break
    else:
        notas.append(float(nota))#Valido que la nota agregada se un float y voy ingresando  cada nota a la lista
        
        
promedio = sum(notas)/len(notas)
print(f"El promedio de las nota es {promedio}")