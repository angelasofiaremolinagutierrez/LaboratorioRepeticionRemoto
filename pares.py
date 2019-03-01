numeros = []
pares = []
impares= []
a = int(input("Ingrese un numero: "))
while (a%2)==0 :
        for b in range(3) :
            print("Número par")
            a = int(input("Ingrese un numero: "))
            par = a
            pares.append (par)
            break
if a%2 != 0:
    impar = a
    impares.append (impar)
    print ("Número impar")

for c in range (1):
    print ("Hay ",len(pares), "número(s) par(es): ", pares)
    print ("Hay ",len(impares), "número(s) impar(es): ", impares)