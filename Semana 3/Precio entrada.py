edad=int(input("Digite la edad de la persona:"))
if ((edad>=0) and (edad<=11)):
    print("Su entrada vale 1000 colones.")
elif ((edad>=12) and (edad<=20)):
    print("Su entrada vaLe 3000 colones.")
elif ((edad>=21) and (edad<=30)):
    print("Su entrada vaLe 4000 colones.")
elif ((edad>=31) and (edad <= 60)):
    print("Su entrada vaLe 5000 colones.")
elif (edad>60):
    print("Puede entrar gratis.")
else:
    print("Edad incorrecta")