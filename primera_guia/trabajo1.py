lista=[12,34,1,9,7,4,2]
numero= int(input("Ingrese el numero a buscar: "))

def fun_buscar(numero):
    print(lista)
    try:
        buscar= lista.index(numero)
        print("Su numero esta en el indice ", buscar)
    except:
        print("El numero no esta en la lista")

fun_buscar(numero)
