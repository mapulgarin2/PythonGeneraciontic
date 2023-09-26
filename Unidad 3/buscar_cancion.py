musica = [("Hollywood Babylon","Misfits",8.9),
          ("Cold feelings","Social Distortion",9.9),
          ("Alien","Pennywise",9.8),
          ("My own country","Pennywise",9.6),
          ("Poison Heart","Ramones",8.0)]

print(type(musica))

def buscar(nombre):
    for cancion in musica:
        if cancion[0]==nombre:
            return cancion
    return None

def buscar_artista(artista):
    lista_artista = []
    for banda in musica:
        if banda[1]==artista:
            lista_artista.append(banda)
    return lista_artista
      
 
print(buscar("Poison Heart"))   
print(buscar_artista("Pennywise")) 
        
        
    