class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        print(f"Modelo {self.modelo}, Marca {self.marca}, Año {self.año}")
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        
    def descripcion(self):
        print(f"Marca {self.marca},Modelo {self.modelo}, Año {self.año}, Numero de Puertas {self.numero_puertas}")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_bicicleta):
        super().__init__(marca, modelo, año)
        self.tipo_bicicleta = tipo_bicicleta
        
    def descripcion(self):
        print(f"Modelo {self.modelo}, Marca {self.marca}, Año {self.año}, Tipo de bicicleta {self.tipo_bicicleta}")
        
coche = Coche("munstang","ford","2000",2)
bicicleta = Bicicleta("montanera","adidas","2024","todo terreno")
print(f"{coche.descripcion()}")
print(f"{bicicleta.descripcion()}")
