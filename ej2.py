class Alumno():

    def inicializar(self, nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        try:
            if(self.nota>=4):
                print("Alumno: ",self.nombre," nota: ",self.nota," estado ","Aprobado")
            else:
                print("Alumno: ",self.nombre," nota: ",self.nota," estado ","Desaprobado")
        except:
            print("No se inizializaron los valores")

'''Aprobado'''
alumno1=Alumno()
alumno1.inicializar("Juan", 3)
alumno1.imprimir()

'''Desaprobado'''
alumno2=Alumno()
alumno2.inicializar("Marcos", 8)
alumno2.imprimir()

'''Sin inizilizar'''
alumno3=Alumno()
alumno3.imprimir()

