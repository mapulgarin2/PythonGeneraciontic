musica = [("Hollywood Babylon","Misfits",8.9),
          ("Cold feelings","Social Distortion",9.9),
          ("Alien","Pennywisw",9.8),
          ("Poison Heart","Ramones",8.0)]

print(type(musica))

def buscar(nombre):
    for cancion in musica:
        if cancion[0]==nombre:
            return cancion
    return None

print(buscar("Poison Heart"))    
        
        
    