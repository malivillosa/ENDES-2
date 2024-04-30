class Articulo:
    def __init__(self, nombre, precio, IVA, stock):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 21
        self.stock = stock

    def PVP(self):
        return self.precio * (1 + self.IVA / 100)

class Main:
    def __init__(self):
        articulo1 = Articulo("Pijama", 10, 21, 5)

        print(f"{articulo1.nombre}, Precio: {articulo1.PVP()}")

Main()