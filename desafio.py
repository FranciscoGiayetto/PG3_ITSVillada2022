import math

cont=0
while(True):
    ancho= int(input("inserte el ancho de de su triangulo(tiene q se un numero impar): "))
    if(ancho%2 == 0):
        print("el numero no es impar")
    else:
         break
    
caracter= input("inserte el caracter de de su triangulo: ")
mitad= math.floor(ancho//2)

for i in range(ancho):
    largo=ancho- i*2
    print(" " * i, caracter* largo  , " " * i  )
    if(i == mitad):
        break

for i in range(ancho):
    espacios=mitad-i
    cont+=1
    print(" " * espacios, caracter* cont  , " " * espacios  )
    cont=cont+1
    if(i == mitad):
        break