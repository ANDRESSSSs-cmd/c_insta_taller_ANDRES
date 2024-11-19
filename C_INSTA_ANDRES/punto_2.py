class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        """
        Inicializa los atributos del material de la biblioteca.
        :param titulo: Título del material (str).
        :param autor: Autor del material (str).
        :param codigo: Código único para identificar el material (str).
        :param disponible: Indica si el material está disponible para préstamo (bool).
        """
        self.titulo = titulo          # Título del material
        self.autor = autor            # Autor del material
        self.codigo = codigo          # Código único para identificar el material
        self.disponible = disponible  # Disponibilidad del material para préstamo

    def prestar(self):
        """Cambia el estado de disponible a False si el material está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"El material '{self.titulo}' ha sido prestado.")
        else:
            print(f"El material '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        """Cambia el estado de disponible a True si el material está prestado."""
        if not self.disponible:
            self.disponible = True
            print(f"El material '{self.titulo}' ha sido devuelto y está disponible para préstamo.")
        else:
            print(f"El material '{self.titulo}' ya está disponible.")

    def mostrar_info(self):
        """Imprime los detalles del material, incluyendo su estado de disponibilidad."""
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"\nDetalles del Material:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código: {self.codigo}")
        print(f"Estado: {disponibilidad}")


# Ejemplo de uso:

# Crear un material de la biblioteca
material1 = MaterialBiblioteca("1984", "George Orwell", "M001")

# Mostrar la información del material
material1.mostrar_info()

# Prestar el material
material1.prestar()

# Mostrar la información después del préstamo
material1.mostrar_info()

# Devolver el material
material1.devolver()

# Mostrar la información después de la devolución
material1.mostrar_info()


