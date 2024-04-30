class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def imprimir(self):
        print(f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellidos}, Edad: {self.edad}")

    def es_mayor_edad(self):
        return self.edad >= 18
    
    def es_jubilado(self):
        return self.edad >= 65
    
    def diferencia_edad(self, p):
        return abs(p.edad - self.edad)

class Main:
    def __init__(self):

        edad = int(input("Dime la edad: "))
        persona1 = Persona("dni1", "nom1", "ape1", edad)
        # Persona 2 para hacer el ejemplo.
        persona2 = Persona("dni2", "nom2", "ape2", 20)
        
        persona1.es_mayor_edad()

        # Esto no nos sirve de nada
        # p= int(input("Dime la edad de diferencia: "))
        
        print("Diferencia de edad: ", persona1.diferencia_edad(persona2))
        

Main()




# class Persona:
#     def __init__(self, dni, nombre, apellidos, edad):
#         self.dni = dni
#         self.nombre = nombre
#         self.apellidos = apellidos
#         self.edad = edad

#     def imprimir(self):
#         print(f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellidos}, Edad: {self.edad}")

#     def es_mayor_edad(self):
#         return self.edad >= 18
    
#     def es_jubilado(self):
#         return self.edad >= 65
    
#     def diferencia_edad(self, p):
#         return abs(p - self.edad)

# class Main:
#     def __init__(self):

#         edad = int(input("Dime la edad: "))
#         persona1 = Persona("dni1", "nom1", "ape1", edad)
        
#         print(persona1.es_mayor_edad())

#         p= int(input("Dime la edad de diferencia: "))
#         print(p.diferencia_edad(p))

# Main()