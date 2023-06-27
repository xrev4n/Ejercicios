lista_telefonos = [{'nombre': 'Pepito', 'telefono': 98510214}, {'nombre': 'Panchito VII', 'telefono': 72840124}, {'nombre': 'Claudia VIII', 'telefono': 75820951}, {'nombre': 'Carlos', 'telefono': 17390121}, {'nombre': 'Michi', 'telefono': 88118811}, {'nombre': 'NotMichi', 'telefono': 11881188}, {'nombre': 'Un perrito', 'telefono': 571924012}, {'nombre': 'Algun tipo que no conozco', 'telefono': 27295012}, {'nombre': 'Jerardo con J', 'telefono': 1279501023}, {'nombre': 'Gustavo', 'telefono': 1982981}, {'nombre': 'Pancha', 'telefono': 12389829}, {'nombre': 'Antonnnnnia', 'telefono': 519391241}, {'nombre': 'Gerardo sin J', 'telefono': 28495012}, {'nombre': 'Tatatatat', 'telefono': 12884192412}, {'nombre': 'Panchin', 'telefono': 12315231}]

def busqueda(cadena):
    resultado = [] #ALMACENA LOS NOMBRES Y NUMEROS ENCONTRADOS
    cadena = cadena.lower() #ALMACENA EL INPUT DEL USUARIO Y LO NORMALIZA CONVIRTIENDO TODOS SUS VALORES A MINUSCULAS
    indexador = 0 #ALMACENA EL INDICE DEL ELEMENTO QUE SE ESTA ITERANDO
    
    for diccionario in lista_telefonos: #ITERA CADA VALOR DE lista_telefonos Y ALMACENA EN LA VARIABLE diccionario EL VALOR QUE SE ESTA ITERANDO
        nombre = diccionario['nombre'].lower() #CREA UNA VARIABLE nombre DONDE ALMACENA EL VALOR DE LA LLAVE 'nombre' CONTENIDA EN EL VALOR QUE SE ESTA ITERANDO ACTUALMENTE (diccionario)
        telefono = str(diccionario['telefono']) #LO MISMO QUE LA LINEA ANTERIOR PERO CON LA LLAVE 'telefono' , SE DEFINE COMO str PARA PODER COMPARARLA CON LA cadena QUE INGRESA EL USUARIO Y ASI FILTRAR LOS TELEFONOS TAMBIEN
    
        if cadena in nombre or cadena in telefono: #CONDICIONAL, ESTABLECE QUE SI EL VALOR DE cadena SE ENCUNETRA DENTRO DE LA VARIABLE nombre O SI EL VALOR DE cadena SE ENCUENTRA EN telefono SE CUMPLE LA CONDICION
            resultado.append((nombre, telefono)) #AGREGA A LA LISTA DE RESULTADOS EL NOMBRE Y EL TELEFONO FILTRADO
            indice = indexador #ASIGNA A LA VARIABLE indice EL VALOR ACTUAL DE INDEXADOR (SI SIMPLEMENTE RETORNAMOS INDEXADOR, NOS DARA EL LARGO TOTAL DE LA LISTA EN VEZ DEL VALOR EN EL CUAL NOS ENCONTRAMOS)
        indexador = indexador + 1 #AUMENTA EL INDEXADOR EN 1, PARA QUE COINCIDA CON EL SIGUIIENTE ELEMENTO DE LA LISTA
    
    return resultado , indice

cadena = input("Ingrese su búsqueda (SI DESEA AGREGAR UN CORREO ASEGURESE DE ESCRIBIR EL NOMBRE EXACTO):\n") #INPUT, PERMITE AL USUARIO INGRESAR LA CADENA DE BUSQUEDA
resultado , indice = busqueda(cadena) #TUPLA, ASIGNA EN LAS VARIABLES resultado E indice LOS RESPECTIVOS VALORES QUE RETORNA LA FUNCION busqueda(cadena)

if len(resultado) > 0: #SI EL RESULTADO DE LA BUSQUEDA ARROJA MAS DE 0 RESULTADOS, LOS IMPRIME
    print(resultado)

if len(resultado) == 1: #SI ARROJA SOLO UN RESULTADO, PERMITE AGREGAR UN CORREO
    decide = int(input("¿Desea agregar un correo?\n1 = SI\n2 = NO\n")) #INPUT, PERMITE AL USUARIO DECIDIR SI AGREGAR O NO UN CORREO

    if decide == 1: #USUARIO ELIGE SI
        correo = input("Ingrese el correo:\n") #ALMACENA EL CORREO QUE INGRESA EL USUARIO
        lista_telefonos[indice]['e-mail'] = correo #MODIFICA LA LISTA, DE MANERA QUE EN EL INDICE QUE NOS RETORNO LA BUSQUEDA (QUE CORRESPONDE AL INDICE DEL NUMERO SELECCIONADO) NOS AGREGA LA LLAVE e-mail Y LE ASIGNA COMO VALOR EL CORREO INGRESADO
        print(lista_telefonos[indice]) #IMPRIME EL ELEMENTO DEL DICCIONARIO YA MODIFICADO CON EL CORREO AGREGADO
    
    if decide == 2:#USUARIO ELIGE NO
        print("Hasta pronto") #EL PROGRAMA TERMINA

if len(resultado) == 0: #SI ARROJA 0 RESULTADOS, IMPRIME MENSAJE DE ERROR
    print("No se encontraron resultados.")
