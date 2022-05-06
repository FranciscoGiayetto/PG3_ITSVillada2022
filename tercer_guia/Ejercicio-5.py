f = open("texto.txt", "w")
f.write("Hola mundo")
try:
    f.write(5)
except TypeError:
    print("Error, no es un string")
f.close()
