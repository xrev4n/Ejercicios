num = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

if ((num * num2) > (num + num2 + num3)):
    print ("La multiplicacion de los dos primeros numeros es mayor a la suma de los tres")
if ((num * num2) < (num + num2 + num3)):
    print ("La multiplicacion de los dos primeros numeros es menor a la suma de los tres")
if ((num * num2) == (num + num2 + num3)):
    print("La multiplicacion de los dos primeros numeros es igual a la suma de los tres")