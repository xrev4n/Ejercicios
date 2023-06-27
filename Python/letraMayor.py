letra1 = str(input("Ingrese la primera letra 🔤:")).lower()
letra2 = str(input("Ingrese la segunda letra 🔤:")).lower()

if ord(letra1) > ord(letra2):
    print("La primera letra es mayor")
elif ord(letra1) < ord(letra2):
    print("La segunda letra es mayor")
else:
    print("Ambas son la misma letra 🤦‍♂️")