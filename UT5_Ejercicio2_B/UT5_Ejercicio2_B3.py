class Rectangulo:
    def __init__(self,x1, y1, x2, y2):
        if x1 < x2 and y1 < y2: 
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

        else:
            self.x1 = 0
            self.y1 = 0
            self.x2 = 0
            self.y2 = 0

            print("Como eres iutil y no sabes poner las coordenadas bien, las he puesto a 0 todes")

    @property
    def distancia_x(self):
        return abs(self.x2 - self.x1)     

    @property
    def distancia_y(self):
        return abs(self.y1 - self.y2)   

    def imprimir_info(self):
        print(f"Las coordenadas son {self.x1}, {self.y1}, {self.x2}, {self.y2}")
    
    def get_perimetro(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))
    
    def get_area(self):
        return abs(self.x2 + self.x1) * abs(self.y2 + self.y1) 

class Main:
    def __init__(self):
        rectangulo1 = Rectangulo(0,0,5,5)
        rectangulo2 = Rectangulo(7,9,2,3)

        print(f"La distancia es: {rectangulo1.distancia_y}")

        
Main()