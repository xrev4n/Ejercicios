def calcular_impuesto(tipo_tributo, tramo_ingresos):
    if tipo_tributo == "PERSONA":
        if tramo_ingresos < 1000000:
            return (tramo_ingresos * 0.05)
        elif tramo_ingresos < 2500000:
            return (tramo_ingresos * 0.07)
        elif tramo_ingresos < 4000000:
            return (tramo_ingresos * 0.12)
        elif tramo_ingresos < 10000000:
            return (tramo_ingresos * 0.16)
        else:
            return (tramo_ingresos * 0.20)
    elif tipo_tributo == "EMPRESA":
        if tramo_ingresos < 1000000:
            return (tramo_ingresos * 0.07)
        elif tramo_ingresos < 2500000:
            return (tramo_ingresos * 0.10)
        elif tramo_ingresos < 4000000:
            return (tramo_ingresos * 0.15)
        elif tramo_ingresos < 10000000:
            return (tramo_ingresos * 0.18)
        else:
            return (tramo_ingresos * 0.22)

tipo_tributo = str(input("Ingrese el tipo de tributo. (PERSONA o EMPRESA)"))
tramo_ingresos = int(input("Escriba sus ingresos mensuales."))

impuesto = calcular_impuesto(tipo_tributo, tramo_ingresos)
print("A usted, le corresponde pagar el", int(impuesto*100/tramo_ingresos), "% de sus ingresos, que corresponden a $", impuesto)
