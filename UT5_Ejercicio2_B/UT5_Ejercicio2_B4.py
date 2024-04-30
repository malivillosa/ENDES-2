class Articulo:
    def __init__(self, nombre, precio, IVA, stock):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 21
        self.stock = stock

    def PVP(self):
        return self.precio * (1 + self.IVA / 100)
    
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Precio: {self.PVP()}, Stock: {self.stock}")

    def get_pvp_descuento(self, d):
        print(self.PVP() - (self.PVP() * (d/100)))

    def vender(self, cantidad):
        if cantidad < self.stock:
            self.stock -= cantidad
            return True
        else:
            print("No hay suficiente stock")
            return False
        
    def almacenar(self, cantidad):
        self.stock += cantidad
        print(self.stock)
        


class Main:
    def __init__(self):
        articulo1 = Articulo("Pijama", 10, 21, 5)

        articulo1.imprimir_info()
        articulo1.get_pvp_descuento(10)
        articulo1.almacenar(10)

Main()