class personas():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad)

class empleado():
    def __init__(self):
        super().__init__()

    def inicializar(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
    def impuestos(self):
        if self.sueldo>=3000:
            print("El empleado: ",self.nombre," tiene un sueldo de: ",self.sueldo," y tiene que pagar impuestos")
        else:
            print("El empleado: ",self.nombre," tiene un sueldo de: ",self.sueldo," y no tiene que pagar impuestos")

persona1=personas("Juan", 20)
persona1.imprimir()
empleado1=empleado()
empleado1.inicializar("Juan", 20, 4000)
empleado1.impuestos()