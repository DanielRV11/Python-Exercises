ingresos=float(input("Digite sus ingresos mensuales: "))
gastosPorAlimentacion= float(input("Digite sus gastos mensuales por alimentación: "))
dineroDisponible=ingresos-gastosPorAlimentacion
porcentajeDisponible=dineroDisponible/ingresos*100
porcentajeDeGastos=gastosPorAlimentacion/ingresos*100
print("El porcentaje que queda para otros gastos es de:",porcentajeDisponible, "%")
print("El porcentaje de gastos en alimentación es de:",porcentajeDeGastos, "%")