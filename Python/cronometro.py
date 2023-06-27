import winsound
import time

frequencia = 2500
duracion = 500
segundos = int(input("Ingrese la cantidad de segundos a contar ⏱️ : "))
contador = 1

while contador != segundos+1:
    print (f"\r⏱️  = {contador}" , end="")
    winsound.Beep(frequencia, duracion)
    contador = contador + 1
    time.sleep(1)