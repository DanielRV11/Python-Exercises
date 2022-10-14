#Se le pide al usuario que escriba los datos para así poder realizar los descuentos.

name=input("Escriba su nombre completo: ")
print("Tenemos a la venta los siguientes productos con sus respectivos descuentos")
print("Num    Tipo \t\t\t\t\t\t\t\t\t\t Descuento")
print("1.     Repuestos para el motor \t\t\t\t\t\t 15% \n2.     Repuestos accesorios \t\t\t\t\t\t 10% \n3.     Repuestos para la limpieza del auto \t\t\t 5% \n4.     Repuestos para los frenos \t\t\t\t\t 3%")
producto=int(input("Marque con el número de identificación del producto que desea comprar: "))

#Se limitan las opciones
if producto>5 or producto<=0:
    print("No contamos con ese producto actualmente")

else:
    cantidad =int(input("Cuántas unidades desea comprar?: "))
    precio= float(input("Digite el precio del producto: "))
    totalsuma= precio*cantidad

    #Se realizan las facturas dependiendo del producto que desee comprar el usuario.

    if producto==1:
        descuento1= totalsuma*0.15
        resta1= totalsuma-descuento1
        print("                   Factura                             ")
        print("Nombre del cliente             ",name)
        print("Producto comprado               Repuestos para el motor")
        print("Cantidad comprada              ",cantidad)
        print("Precio unitario del producto   ",precio,"colones")
        print("Precio total por cantidad      ",totalsuma,"colones")
        print("Descuento                      ",descuento1,"colones")
        print("Precio final                   ",resta1,"colones")

    elif producto==2:
        descuento2= totalsuma*0.10
        resta2= totalsuma-descuento2
        print("                   Factura                             ")
        print("Nombre del cliente             ",name)
        print("Producto comprado               Repuestos accesorios")
        print("Cantidad comprada              ",cantidad)
        print("Precio unitario del producto   ",precio,"colones")
        print("Precio total por cantidad      ",totalsuma,"colones")
        print("Descuento                      ",descuento2,"colones")
        print("Precio final                   ",resta2,"colones")

    elif producto==3:
        descuento3= totalsuma*0.05
        resta3= totalsuma-descuento3
        print("                   Factura                             ")
        print("Nombre del cliente             ",name)
        print("Producto comprado               Repuestos para la limpieza del auto")
        print("Cantidad comprada              ",cantidad)
        print("Precio unitario del producto   ",precio,"colones")
        print("Precio total por cantidad      ",totalsuma,"colones")
        print("Descuento                      ",descuento3,"colones")
        print("Precio final                   ",resta3,"colones")

    elif producto==4:
        descuento4= totalsuma*0.03
        resta4= totalsuma-descuento4
        print("                   Factura                             ")
        print("Nombre del cliente             ",name)
        print("Producto comprado               Repuestos para los frenos")
        print("Cantidad comprada              ",cantidad)
        print("Precio unitario del producto   ",precio,"colones")
        print("Precio total por cantidad      ",totalsuma,"colones")
        print("Descuento                      ",descuento4,"colones")
        print("Precio final                   ",resta4,"colones")