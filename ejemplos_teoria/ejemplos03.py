class Animal:
    def __init__(self, name):
        self.name = name

    def hablar(self):
        return f"{self.name} hace un sonido."

class Perro(Animal):
    def __init__(self, name, raza):
        super().__init__(name)
        self.raza = raza

    def hablar(self):
        return f"{self.name}, el {self.raza}, hace un sonido."

perro = Perro("Max", "Labrador")
print(perro.hablar())  # Max, el Labrador, hace un sonido.
