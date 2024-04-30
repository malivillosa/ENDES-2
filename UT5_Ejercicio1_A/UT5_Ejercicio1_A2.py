class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return f"{self.dni}, {self.nombre}, {self.apellidos}, {self.edad}"

class Main:
    def __init__(self):
        persona1 = Persona("dni1", "nom1", "ape1", "edad1")
        persona2 = Persona("d", "n", "a", 10)

        dni_p = input("Dame el dni: ")
        nom_p = input("Dame el nom: ")
        ape_p = input("Dame el ape: ")
        eda_p = int(input("Dame la eda: "))

        persona3 = Persona(dni_p, nom_p, ape_p, eda_p)

        if persona3.edad >= 18:
            print(f"{persona3.nombre} con dni {persona3.dni} es mayor de edad")
        else:
            print(f"{persona3.nombre} con dni {persona3.dni} no es mayor de edad")

        
        # print(persona2)
        # print(persona3)

Main()