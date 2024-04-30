class Rectangulo:
    def __init__(self,x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def perimetro(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))
    
    def area(self):
        return abs(self.x2 + self.x1) * abs(self.y2 + self.y1) 

class Main:
    def __init__(self):
        rectangulo1 = Rectangulo(0,0,5,5)
        rectangulo2 = Rectangulo(7,9,2,3)

        print("Las coordenadas son:")
        print(f"({rectangulo1.x1}, {rectangulo1.y1}), ({rectangulo1.x2}, {rectangulo1.y2})")
        print("El perimetro es:", rectangulo1.perimetro())
        print("El area es:", rectangulo1.area())
        
Main()