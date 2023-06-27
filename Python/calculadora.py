num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
op = str(input("Escriba la operacion (SUMA , RESTA , MULTIPLICACION , DIVISION): "))

if (op == "SUMA"):
    print ("El resultado es" , (num + num2))
if (op == "RESTA"):
    print ("El resultado es" , (num - num2))
if (op == "MULTIPLICACION"):
    print ("El resultado es" , (num * num2))
if (op == "DIVISION"):
    print ("El resultado es" , (num / num2))

