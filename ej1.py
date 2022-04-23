class persona():
    def inicializar(self, nombre):
        self.nombre=nombre
    def imprimir(self):
        try:
            print("Nombre: ", self.nombre)
        except AttributeError:
            print("No iniciaste la persona")


persona1=persona()
persona1.inicializar("Juan")
persona1.imprimir()

persona2=persona()
persona2.inicializar("Marcos")
persona2.imprimir()

persona3=persona()
persona3.imprimir()


