class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo  # Título del material
        self.autor = autor  # Autor del material
        self.codigo = codigo  # Código único para identificar el material
        self.disponible = disponible  # Disponibilidad para préstamo (por defecto True)

    def mostrar_informacion(self):
        """Muestra la información del material."""
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código: {self.codigo}")
        print(f"Estado: {disponibilidad}")

    def prestar(self):
        """Marca el material como prestado si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"El material '{self.titulo}' ha sido prestado.")
        else:
            print(f"El material '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        """Marca el material como disponible para préstamo."""
        if not self.disponible:
            self.disponible = True
            print(f"El material '{self.titulo}' ha sido devuelto y está disponible para préstamo.")
        else:
            print(f"El material '{self.titulo}' ya está disponible.")

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.genero = genero  # Atributo específico de los libros

    def mostrar_informacion(self):
        """Sobrescribimos el método para incluir el género"""
        super().mostrar_informacion()  # Llamamos al método de la clase base
        print(f"Género: {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, periodicidad, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.periodicidad = periodicidad  # Atributo específico de las revistas

    def mostrar_informacion(self):
        """Sobrescribimos el método para incluir la periodicidad"""
        super().mostrar_informacion()  # Llamamos al método de la clase base
        print(f"Periodicidad: {self.periodicidad}")

# Crear instancias de libros y revistas
libro1 = Libro("El Quijote", "Miguel de Cervantes", "LIB001", "Novela")
revista1 = Revista("National Geographic", "Varios", "REV001", "Mensual")

# Mostrar la información de los materiales
libro1.mostrar_informacion()
print("---")
revista1.mostrar_informacion()
print("---")

# Probar la funcionalidad de préstamo y devolución
libro1.prestar()  # Debería marcarlo como no disponible
libro1.mostrar_informacion()  # Mostrar la información actualizada

print("---")
revista1.prestar()  # Debería marcarla como no disponible
revista1.mostrar_informacion()  # Mostrar la información actualizada

# Devolver materiales
libro1.devolver()
revista1.devolver()
