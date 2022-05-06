while True:
    num1 = 0
    num2 = 0
    try:
        num1 = int(input("Ingrese un numero: "))
    except ValueError:
        print("Error, no es un numero")

    try:
        num2 = int(input("Ingrese otro numero: "))
    except ValueError:
        print("Error, no es un numero")
    else:
        suma = num1 + num2
        print("La suma de los numeros es: ", suma)
        print("queres seguir sumando? (si/no)")
        respuesta = input()
        if respuesta == "no":
            break
