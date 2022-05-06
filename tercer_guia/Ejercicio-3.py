while True:
    num_mes = input("Ingrese el numero del mes: ")
    try:
        num_mes = int(num_mes)
    except ValueError:
        print("Error, no es un numero")
    else:
        if num_mes == 1:
            print("Enero")
        elif num_mes == 2:
            print("Febrero")
        elif num_mes == 3:
            print("Marzo")
        elif num_mes == 4:
            print("Abril")
        elif num_mes == 5:
            print("Mayo")
        elif num_mes == 6:
            print("Junio")
        elif num_mes == 7:
            print("Julio")
        elif num_mes == 8:
            print("Agosto")
        elif num_mes == 9:
            print("Septiembre")
        elif num_mes == 10:
            print("Octubre")
        elif num_mes == 11:
            print("Noviembre")
        elif num_mes == 12:
            print("Diciembre")
        else:
            print("Error, no es un numero del 1 al 12")
        print("queres seguir? (si/no)")
        respuesta = input()
        if respuesta == "no":
            break
