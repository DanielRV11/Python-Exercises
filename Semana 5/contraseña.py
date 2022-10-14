usuario=""
clave=""
while usuario!= "admin" or clave != "123":
    usuario=input("Usuario: ")
    clave=input("Clave: ")
    if usuario=="admin" and clave=="123":
        print("Bienvenido")
    else:
        print("Error, intente otra vez.")