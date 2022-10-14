counter = 0
suma_edades = 0
while counter < 5:
    counter += 1
    edad = int(input("Ingrese la edad " + str(counter) + ": "))
    suma_edades += edad
total = suma_edades / 5
print("Promedio", total)