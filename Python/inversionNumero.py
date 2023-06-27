numero = int(input("Ingrese un numero entero positivo: "))
inversion = str("")

while numero > 0:
    modulo = (numero%10)
    inversion = f"{inversion}" + f"{modulo}"
    numero = (numero//10)

print(inversion)
