def step(numero):
    primero = map(int, str(numero)[1:]) 
    segundo = map(int, str(numero)[:-1])
    return all(abs(primero_p - segundo_p) == 1 for primero_p, segundo_p in zip(primero, segundo))




Numero = int(input("Ingrese un numero "))
if(step(Numero) == True):
    print("El numero es step")
else:
    print("El numero no es step") 