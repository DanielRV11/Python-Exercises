edad=int(input("Digite su edad:"))
if edad<18:
    print("Aún no eres mayor de edad.")
elif edad==18:
    print("Los acabas de cumplir.")
elif edad==19:
    print("Hace 1 año tenías 18 años.")
else:
    nuevaEdad=(edad-18)
    print("Hace",nuevaEdad,"años tenías 18 años.")