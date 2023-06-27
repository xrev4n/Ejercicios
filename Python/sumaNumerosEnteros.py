numero = int(input("Ingrese un número positivo: "))
suma = 0
ultimo_digito = 0

while numero > 0:
    ultimo_digito = numero % 10
    suma += ultimo_digito
    numero //= 10

print(f"La suma de los numeros es: {suma}")