##Ejemplo pregunta 02
class A:
    def saludar(self):
        return "Hola de A"

class B:
    def saludar(self):
        return "Hola de B"

class C(A, B):
    pass

c = C()
print(c.saludar())  # "Hola de A" ya que A aparece antes en la lista de herencia.
