frase= input("ingrese su frase: ")
contador=0
lista=[]
lista= list(str(frase.lower()))
print(str(frase.lower()))


for i in range(len(lista)):
    if (lista[i] == "a" or lista[i] == "i" or lista[i] == "e" or lista[i] == "o" or lista[i] == "u"):
        contador= contador + 1
print(contador)