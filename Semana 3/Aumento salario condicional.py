nuevoSalario=0
salarioActual=float(input("Digite el salario actual del empleado:"))
antiguedad=int(input("Digite los años que lleva laburando el empleado"))
if ((antiguedad>=0) and (antiguedad<=5)):
    nuevoSalario=salarioActual*1.01
elif ((antiguedad>=6) and (antiguedad<=10)):
    nuevoSalario=salarioActual*1.03
elif ((antiguedad>=11) and (antiguedad<=13)):
    nuevoSalario=salarioActual*1.05
else:
    nuevoSalario=salarioActual*1.07
print("El salario luego del aumento es de:",nuevoSalario)