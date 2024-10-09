class Motor:
    def encender(self):
        return "Encendiendo motor"

class Carro:
    def __init__(self):
        self.Motor = Motor()

    def encender(self):
        return self.Motor.encender() + ", y el carro se mueve"

carro = Carro()
print(carro.encender())  #Encendiendo motor, y el carro se mueve
