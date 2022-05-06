print("cuando quiera frenar ponga f")
lista=[]
while(True):
    numero=input()
    if(numero== "f"):
        break
    lista.append(int(numero))
    print("tu lista actual es: ",lista)

print(sorted(lista, reverse=True))
