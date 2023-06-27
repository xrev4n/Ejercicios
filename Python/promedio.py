num = 0
suma = 0
promedio = 0
contador = 0

while (True):
    num = 2
    if num == 0:
        break
    suma = suma + num
    contador = contador + 1
    promedio = suma/contador
    print(f"El promedio es de : {promedio}")
    