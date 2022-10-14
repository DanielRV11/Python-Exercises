nuevoSalario=0
salarioActual=float(input("Cuál es su salario actual?"))
antiguedad=int(input("Cuántos años lleva laburando?"))
if (antiguedad>5):
    nuevoSalario=salarioActual*1.10
    print("El nuevo salario del empleado es de:", nuevoSalario)
elif (antiguedad<5):
    print("El salario es de:",salarioActual)
