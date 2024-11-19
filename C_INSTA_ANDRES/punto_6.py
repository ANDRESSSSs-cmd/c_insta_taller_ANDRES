# Clase base Mascota
class Mascota:
    def __init__(self, nombre, edad, especie):
        """
        Inicializa los atributos de la mascota.
        :param nombre: Nombre de la mascota (str).
        :param edad: Edad de la mascota (int).
        :param especie: Especie de la mascota (str).
        """
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        """Imprime los detalles básicos de la mascota."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Especie: {self.especie}")


# Clase hija Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        """
        Inicializa los atributos del perro, heredados de Mascota y adicionales.
        :param raza: Raza del perro (str).
        """
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def ladrar(self):
        """Método que simula el ladrido del perro."""
        print("Guau, guau")

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir la raza."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Raza: {self.raza}")


# Clase hija Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        """
        Inicializa los atributos del gato, heredados de Mascota y adicionales.
        :param color: Color del gato (str).
        """
        super().__init__(nombre, edad, especie)
        self.color = color

    def maullar(self):
        """Método que simula el maullido del gato."""
        print("Miau")

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el color."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Color: {self.color}")


# Ejemplo de uso:

# Crear un perro
perro1 = Perro("Rex", 3, "Perro", "Labrador")

# Crear un gato
gato1 = Gato("Mimi", 2, "Gato", "Negro")

# Mostrar la información del perro
print("\nInformación del Perro:")
perro1.mostrar_info()
perro1.ladrar()  # El perro ladra

# Mostrar la información del gato
print("\nInformación del Gato:")
gato1.mostrar_info()
gato1.maullar()  # El gato maulla
