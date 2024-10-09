class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

libro01 = Libro("Python Basics")
libro02 = Libro("Advanced Python")
Libreria = Libreria()
Libreria.agregar_libro(libro01)
Libreria.agregar_libro(libro02)
for libro in Libreria.libros:       # Python Basics
    print(libro.titulo)             # Advanced Python
    

