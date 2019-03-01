numeros = []
mayores = []
menores = []
ceros = []
for datos in range(3) :
    a = int(input("Ingrese un numero: "))
    numeros.append (a)

    if a > 0:
        mayor = a
        mayores.append (mayor)
        print("Número mayor que cero")
    elif a < 0:
        menor = a
        menores.append (menor)
        print ("Número menor a cero")
    else :
        cero = a
        ceros.append (cero)
        print ("El número es cero")

for datos in range (1):
    print ("Hay ",len(mayores), "número(s) mayor(es) que cero: ", mayores)
    print ("Hay ",len(menores), "número(s) menor(es) que cero: ", menores)
    print ("Hay ",len(ceros), "ceros: ", ceros)