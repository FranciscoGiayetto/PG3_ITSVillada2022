class calculadora():
    def __init__(self):
        self.num1=int(input("Ingrese el primer numero: "))
        self.num2=int(input("Ingrese el segundo numero: "))
        self.suma(self.num1,self.num2)
        self.resta(self.num1,self.num2)
        self.multiplicacion(self.num1,self.num2)
        self.division(self.num1,self.num2)

    def suma(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("suma: ",self.num1 + self.num2) 

    def resta(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("resta: ",self.num1 - self.num2) 

    def multiplicacion(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("multiplicacion: ",self.num1 * self.num2) 

    def division(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("division: ",self.num1 / self.num2) 
calculadora1=calculadora()
calculadora1.__init__()