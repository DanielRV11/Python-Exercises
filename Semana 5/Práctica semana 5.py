#Se realizaron las variables
seguir="s"
letra=""

#Se completó el ciclo
while (seguir=="s"):
    letra = input("Digite una letra: ")
    #reconoce las vocales
    if letra=="a" or letra== "e" or letra== "i" or letra== "o" or letra== "u":
        print("Es una vocal.")
    #reconoce las vocales en mayúsculas
    elif letra=="A" or letra== "E" or letra== "I" or letra== "O" or letra== "U":
        print("Es una vocal.")
    #si no se ingresa ninguna vocal imprime que no es vocal
    else:
        print("No es una vocal.")

    seguir=input("Desea seguir (s/n)?: ")
#si no se desea continuar, imprime un mensaje de despedida
print("Hasta pronto!")

