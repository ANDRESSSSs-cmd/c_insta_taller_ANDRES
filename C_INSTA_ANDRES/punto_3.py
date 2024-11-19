from datetime import datetime

# Clase base MaterialBiblioteca
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


# Clase hija Libro
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        """
        Inicializa los atributos del libro, heredados de MaterialBiblioteca y adicionales.
        :param numero_paginas: Número de páginas del libro (int).
        :param genero: Género literario del libro (str).
        """
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas  # Número de páginas del libro
        self.genero = genero                  # Género literario del libro

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir los detalles del libro."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Número de Páginas: {self.numero_paginas}")
        print(f"Género: {self.genero}")


# Clase hija Revista
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        """
        Inicializa los atributos de la revista, heredados de MaterialBiblioteca y adicionales.
        :param numero_edicion: Número de edición de la revista (int).
        :param fecha_publicacion: Fecha de publicación de la revista (str o datetime).
        """
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion              # Número de edición de la revista
        self.fecha_publicacion = fecha_publicacion        # Fecha de publicación

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir los detalles de la revista."""
        super().mostrar_info()  # Llamamos al método de la clase base
        # Si la fecha de publicación es una cadena, intentamos convertirla a un objeto datetime
        if isinstance(self.fecha_publicacion, str):
            try:
                self.fecha_publicacion = datetime.strptime(self.fecha_publicacion, "%d/%m/%Y")
            except ValueError:
                print("Error al formatear la fecha de publicación. El formato esperado es dd/mm/yyyy.")
        print(f"Número de Edición: {self.numero_edicion}")
        print(f"Fecha de Publicación: {self.fecha_publicacion.strftime('%d/%m/%Y')}")


# Ejemplo de uso:

# Crear un libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "LIB1001", 417, "Realismo mágico")

# Crear una revista
revista1 = Revista("National Geographic", "Varios", "REV1001", 230, "15/10/2023")

# Mostrar la información del libro
print("\nInformación del Libro:")
libro1.mostrar_info()

# Mostrar la información de la revista
print("\nInformación de la Revista:")
revista1.mostrar_info()

# Prestar y devolver el libro
print("\nPréstamo y devolución del libro:")
libro1.prestar()
libro1.devolver()

# Prestar y devolver la revista
print("\nPréstamo y devolución de la revista:")
revista1.prestar()
revista1.devolver()
