#Composición:
class Libro():
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        
class Estudiante():
    def __init__(self,nombre,numero_estudiante):
        self.nombre = nombre
        self.numero_estudiante = numero_estudiante
        
class Biblioteca():
    def __init__(self):
        self.libros = []
        self.estudiantes = []
        
    def agregar_libro(self,titulo,autor,isbn):
        libro = Libro(titulo,autor,isbn)
        self.libros.append(libro)
        print(f"Libro {libro.titulo} agregado con exito")
        
    def agregar_estudiante(self,Estudiante):
        self.estudiantes.append(Estudiante)
        print(f"Estudiante {Estudiante.nombre} gregado con exito")
        
    def eliminar_libro(self,isbn):
        for libro in self.libros:
            if isbn == libro.isbn:
                self.libros.remove(libro)
                print(f"Se ha eliminado el libro con isbn: {isbn}")
                return
        print(f"No se ha encontrado, Ningun libro con isbn: {isbn}")
        
    def eliminar_estudiante(self,numero_estudiante):
        for estudiante in self.estudiantes:
            if numero_estudiante == estudiante.numero_estudiante:
                self.estudiantes.remove(estudiante)
                print(f"Se ha eliminado el estudiante con el numero: {numero_estudiante}")
                return
        print(f"No se ha encontrado, Ningun estudiante con numero: {numero_estudiante}")
        
    def mostrar_libros(self):
        if self.libros:
            for libro in self.libros:
                print(f"titulo: {libro.titulo}, autor: {libro.autor}, isbn: {libro.isbn}")
            return
        print("No se ha encontrado libros en la biblioteca")
        
    def mostrar_estudiantes(self):
        if self.estudiantes:
            for estudiante in self.estudiantes:
                print(f"Nombre: {estudiante.nombre}, numero de estudiante: {estudiante.numero_estudiante}")
            return
        print("No se ha encontrado estudiantes en la biblioteca")
        
        

# Ejemplo de uso
biblioteca = Biblioteca()

estudiante1 = Estudiante("Gabriel Mendoza", "E001")
estudiante2 = Estudiante("Ana Pérez", "E002")

# Agregar libros
biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "979")
biblioteca.agregar_libro("El Quijote", "Miguel de Cervantes", "978")


# mostrar libros
biblioteca.mostrar_libros()

# Eliminar libro
biblioteca.eliminar_libro("978")
biblioteca.mostrar_libros()

# Agregar estudiantes
biblioteca.agregar_estudiante(estudiante1)
biblioteca.agregar_estudiante(estudiante2)

# mostrar estudiantes
biblioteca.mostrar_estudiantes()

# Eliminar estudiante
biblioteca.eliminar_estudiante("E002")
biblioteca.mostrar_estudiantes()
    