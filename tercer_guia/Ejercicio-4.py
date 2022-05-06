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
        div = 0
        try:
            div = num1 // num2
        except ZeroDivisionError:
            print("Error, no se puede dividir entre 0")
        else:
            print("La division de los numeros es: ", div)
            print("queres seguir division? (si/no)")
            respuesta = input()
            if respuesta == "no":
                break
