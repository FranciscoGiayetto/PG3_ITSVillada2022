class Triangulo():
    def inizializar(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            self.mayor=self.lado1
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            self.mayor=self.lado2
        else:
            self.mayor=self.lado3
    def imprimir(self):
        print("El lado mayor es:",self.mayor)
        if self.lado1==self.lado2 and self.lado2==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("no es equilatero")

trinagulo1=Triangulo()
trinagulo1.inizializar(1,2,3)
trinagulo1.imprimir()

triangulo2=Triangulo()
triangulo2.inizializar(4,4,4)
triangulo2.imprimir()
        
