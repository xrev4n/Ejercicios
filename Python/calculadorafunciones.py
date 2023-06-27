def sumar (num1, num2):
    resultado = num1 + num2
    return resultado
def restar (num1, num2):
    resultado = num1 - num2
    return resultado
def dividir (num1, num2):
    resultado = num1 / num2
    return resultado
def multiplicar (num1, num2):
    resultado = num1 * num2
    return resultado
num1 = int(input("Ingresa el primer numero = "))
num2 = int(input("Ingresa el segundo numero = "))
operacion = str(input("Ingresa la operacion\n-SUMAR\n-RESTAR\n-DIVIDIR\n-MULTIPLICAR\n"))
resultado = eval(operacion.lower() + "(num1, num2)")
print(f"El resultado es {resultado} 🤓☝️")