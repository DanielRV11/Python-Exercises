nombre=input("Digite el nombre del funcionario:")
apellido1=input("Digite el primer apellido del funcionario:")
apellido2=input("Digite el segundo apellido del funcionario:")

cedula=int(input("Digite el número de identificación:"))
salarioBruto=float(input("Digite el salario bruto:"))
deduccionCCSS=salarioBruto*0.08
deduccionBP=salarioBruto*0.01
deduccionTotal=deduccionCCSS+deduccionBP
salarioNeto=salarioBruto-deduccionTotal

print("Nombre                     ",nombre,apellido1,apellido2)
print("Identificación             ",cedula)
print("Salario Bruto              ",salarioBruto)
print("CCSS  (8%)                 ",deduccionCCSS)
print("Banco Popular              ",deduccionBP)
print("Total deducciones          ",deduccionTotal)
print("Salario Neto               ",salarioNeto)