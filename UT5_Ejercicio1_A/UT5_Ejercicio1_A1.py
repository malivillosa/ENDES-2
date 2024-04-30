class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"({self.x, self.y})"
        
class Main():
    def __init__(self):
        #Instancia 3 objetos:
        objeto1 = Punto(5, 0)
        objeto2 = Punto(10, 10)
        objeto3 = Punto(-3, 7)
        
         # Imprimirlos
        print(objeto1.x, objeto1.y)
        print(objeto2.x, objeto2.y)
        print(objeto3.x, objeto3.y)

        #Cambiar valores
        objeto1.x += 5
        objeto1.y = 10

        #Imprimir otra vez
        print(objeto1.x, objeto1.y)
Main()