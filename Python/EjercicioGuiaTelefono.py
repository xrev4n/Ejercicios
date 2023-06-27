lista_telefonos = [{'nombre': 'Pepito', 'telefono': 98510214}, {'nombre': 'Panchito VII', 'telefono': 72840124}, {'nombre': 'Claudia VIII', 'telefono': 75820951}, {'nombre': 'Carlos', 'telefono': 17390121}, {'nombre': 'Michi', 'telefono': 88118811}, {'nombre': 'NotMichi', 'telefono': 11881188}, {'nombre': 'Un perrito', 'telefono': 571924012}, {'nombre': 'Algun tipo que no conozco', 'telefono': 27295012}, {'nombre': 'Jerardo con J', 'telefono': 1279501023}, {'nombre': 'Gustavo', 'telefono': 1982981}, {'nombre': 'Pancha', 'telefono': 12389829}, {'nombre': 'Antonnnnnia', 'telefono': 519391241}, {'nombre': 'Gerardo sin J', 'telefono': 28495012}, {'nombre': 'Tatatatat', 'telefono': 12884192412}, {'nombre': 'Panchin', 'telefono': 12315231}]
def busqueda(cadena):
    resultado = [] #ALMACENA LOS NOMBRES Y NUMEROS ENCONTRADOS
    cadena = cadena.lower() #ALMACENA EL INPUT DEL USUARIO
    indexador = 0 #ALMACENA EL INDICE DEL ELEMENTO QUE SE ESTA ITERANDO
    for diccionario in lista_telefonos:
        nombre = diccionario['nombre'].lower()
        telefono = str(diccionario['telefono'])
        if cadena in nombre or cadena in telefono:
            resultado.append((nombre, telefono))
            indice = indexador
        indexador = indexador + 1 #AUMENTA EL INDEXADOR EN 1, PARA QUE COINCIDA CON EL SIGUIIENTE ELEMENTO DE LA LISTA
    return resultado , indice
print(lista_telefonos)    
cadena = input("Ingrese su búsqueda: ")
resultado = busqueda(cadena)
if len(resultado) > 0:
    print(resultado)
if len(resultado) == 2:
    decide = int(input("Desea agregar un correo?\n1 = SI\n2 = NO"))
    if decide == 1:
        correo = input("Ingrese el correo")        
else:
    print("No se encontraron resultados")
