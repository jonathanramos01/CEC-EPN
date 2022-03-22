

Nombre=input("NOMBRE:")
Apellido=input("APELLIDO:")
edad=int(input("EDAD:"))
Ciudad=input("CIUDAD:")
space=" "
if edad>=1 and edad<=10:
    print("Es un niño")
elif edad>=11 and edad<=17:
    print("Es un adolescente")
elif edad>=18 and edad<=60:
    print("Es un adulto")
else:
    print("Es un adulto mayor")
    

print("¡HOLA!", Nombre, Apellido, "TU EDAD ES ",edad,"AÑOS, ", "Y ERES DE LA CIUDAD DE: F",Ciudad,  )