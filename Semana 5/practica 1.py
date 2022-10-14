montoInicial=1500
interesAnual=0.15
montoFinal=montoInicial
for x in range(60):
    montoFinal *= 1+interesAnual

print("El monto inicial de ahorro fue:",montoInicial)
print("EL monto final después de 60 años es: ",montoFinal)