class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"({self.x, self.y})"
        
    def imprimir(self):
        print(f"{self.x}, {self.y}")

    def set_xy(self,x,y):
        self.x = x
        self.y = y
    
    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy
        
class Main():
    def __init__(self):
        #Instancia 3 objetos:
        objeto1 = Punto(5, 0)
        objeto2 = Punto(10, 10)
        objeto3 = Punto(-3, 7)

        objeto2.imprimir()

        objeto2.set_xy(4,6)

        objeto2.imprimir()

        objeto3.desplaza(10,10)

        objeto3.imprimir()
Main()