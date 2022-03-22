
while True:
    numero=input("Ingrese el # al que contare: ")
    if numero == "q" or numero == "quit":
        break
    numero=int(numero)
    contador=1
    while True:
        print(contador)
        contador+=1
        if contador>numero:
            break
    


