suma=0
cargas=0

for i in range(10):
    salario=float(input("Ingrese el salario: "))
    suma += salario

cargas=suma *0.09
print("El total a pagar de salarios es de:",suma,"y las cargas sociales son",cargas)