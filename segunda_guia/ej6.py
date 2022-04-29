class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        ListaHijos = " ".join(str(item) for item in self.hijos)
        return (
            "Padre: "
            + self.padre
            + "\nMadre: "
            + self.madre
            + "\nHijos: "
            + ListaHijos
            + "\n"
        )


print("Familia 1: ")
familia1 = Familia("Juan", "Maria", ["Juan", "Maria", "Jose"])
print(familia1)
print("Familia 2: ")
familia2 = Familia("Agustin", "Antonela", ["Juan", "Pepe", "Yolanda"])
print(familia2)
print("Familia 3: ")
familia3 = Familia("Jose", "Jorge", ["Esteban", "Nestor"])
print(familia3)
