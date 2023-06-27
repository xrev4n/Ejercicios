tipoTributo = str(input("Ingrese el tipo de tributo. (PERSONA o EMPRESA)"))
tramoIngresos = int(input("Escriba sus ingresos mensuales."))

if (tipoTributo == "PERSONA"):
    if (tramoIngresos < 1000000):
        print ("A usted, le corresponde pagar el 5% de sus ingresos, que corresponden a $" , ((tramoIngresos * 5) / 100))
    if (tramoIngresos >= 1000000) and (tramoIngresos < 2500000):
        print ("A usted, le corresponde pagar el 7% de sus ingresos, que corresponden a $" , ((tramoIngresos * 7) / 100))
    if (tramoIngresos >= 2500000) and (tramoIngresos < 4000000):
        print ("A usted, le corresponde pagar el 12% de sus ingresos, que corresponden a $" , ((tramoIngresos * 12) / 100))
    if (tramoIngresos >= 4000000) and (tramoIngresos < 10000000):
        print ("A usted, le corresponde pagar el 16% de sus ingresos, que corresponden a $" , ((tramoIngresos * 16) / 100))
    if (tramoIngresos >= 10000000):
        print ("A usted, le corresponde pagar el 20% de sus ingresos, que corresponden a $" , ((tramoIngresos * 20) / 100))

if (tipoTributo == "EMPRESA"):
    if (tramoIngresos < 1000000):
        print ("A usted, le corresponde pagar el 7% de sus ingresos, que corresponden a $" , ((tramoIngresos * 7) / 100))
    if (tramoIngresos >= 1000000) and (tramoIngresos < 2500000):
        print ("A usted, le corresponde pagar el 10% de sus ingresos, que corresponden a $" , ((tramoIngresos * 10) / 100))
    if (tramoIngresos >= 2500000) and (tramoIngresos < 4000000):
        print ("A usted, le corresponde pagar el 15% de sus ingresos, que corresponden a $" , ((tramoIngresos * 15) / 100))
    if (tramoIngresos >= 4000000) and (tramoIngresos < 10000000):
        print ("A usted, le corresponde pagar el 18% de sus ingresos, que corresponden a $" , ((tramoIngresos * 18) / 100))
    if (tramoIngresos >= 10000000):
        print ("A usted, le corresponde pagar el 22% de sus ingresos, que corresponden a $" , ((tramoIngresos * 22) / 100))