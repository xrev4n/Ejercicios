numero = int(input("Ingrese un numero entero del 0 al 100: "))
porcentaje = round(numero/5)
carga = ("🟩"*porcentaje)
barra = ("⬜"*(20-porcentaje))

print(f"{carga}{barra}")