edad=0
cantidadMayores=0
cantidadMenores=0
seguir="s"
while(seguir=="s"):
    edad=int(input("Digite la edad de la persona: "))
    if(edad>=18):
        cantidadMayores=cantidadMayores+1
    else:
        cantidadMenores=cantidadMenores+1
    seguir=input("Desea seguir (s/n?)")
print("La canridad de personas mayores es:",cantidadMayores,
      "y la cantidad de personas menores es:",cantidadMenores)