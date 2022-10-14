#Se pide al cliente que escriba los productos que desea comprar
producto1=input("¿Que productos desea comprar?:")
producto2=input(":")
producto3=input(":")

#Se le pide al cliente que escriba la canitdad de cada producto que desea comprar
cantidad1=int(input("¿Que cantidad de "+producto1+" desea comprar?: "))
cantidad2=int(input("¿Que cantidad de "+producto2+" desea comprar?: "))
cantidad3=int(input("¿Que cantidad de "+producto3+" desea comprar?: "))

#Se le pide al cliente que por favor escriba los precios de los productos que desea comprar
precio1=float(input("Digite el precio de "+producto1+":"))
precio2=float(input("Digite el precio de "+producto2+":"))
precio3=float(input("Digite el precio de "+producto3+":"))

#Se hacen los cálculos del subtotal de cada producto que desean comprar y la suma de los 3
total1=(precio1*cantidad1)
total2=(precio2*cantidad2)
total3=(precio3*cantidad3)
subtotal=total1+total2+total3

#Se hacen los descuentos y los impuestos de la compra
descuento=subtotal*0.10
precioConDescuento=subtotal-descuento
impuestos=precioConDescuento*0.13

total=subtotal-descuento+impuestos
#Se imprimen los resultados

print("                              Factura                          ")
print("Producto              Cantidad       Precio           Subtotal    ")
print(producto1,"\t\t\t\t\t",cantidad1,"\t\t\t",precio1,"\t\t\t",total1 )
print(producto2,"\t\t\t\t\t",cantidad2,"\t\t\t",precio2,"\t\t\t",total2 )
print(producto3,"\t\t\t\t\t",cantidad3,"\t\t\t",precio3,"\t\t\t",total3 )
print("Subtotal\t\t\t\t\t\t\t\t\t\t\t",subtotal)
print("Descuento 10%\t\t\t\t\t\t\t\t\t\t",descuento)
print("Impuesto 13%\t\t\t\t\t\t\t\t\t\t",impuestos)
print("  ")
print("Total\t\t\t\t\t\t\t\t\t\t\t\t",total)