horasSemanales=int(input("Cuántas horas trabaja semanalmente? "))
precioPorHora=float(input("A cuánto le pagan la hora? "))

salarioBrutoMensual= horasSemanales * 4.2 * precioPorHora
deduccion=salarioBrutoMensual*0.105*0.05
gananciasConCargasSociales=salarioBrutoMensual-(deduccion)
print("El salario bruto mensual es de:",salarioBrutoMensual," y el salalario neto sería de:",gananciasConCargasSociales)
