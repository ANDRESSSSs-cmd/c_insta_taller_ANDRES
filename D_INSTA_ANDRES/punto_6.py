class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        """
        Inicializa los atributos del animal.
        :param nombre: Nombre del animal (str).
        :param especie: Especie del animal (str).
        :param edad: Edad del animal (int).
        :param habitat: Hábitat del animal (str).
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        """Incrementa la edad del animal en un año."""
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")

    def cambiar_habitat(self, nuevo_habitat):
        """Modifica el hábitat del animal."""
        self.habitat = nuevo_habitat
        print(f"{self.nombre} ahora vive en {self.habitat}.")

    def mostrar_detalles(self):
        """Imprime los detalles completos del animal."""
        print(f"Detalles del Animal:")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")


# Ejemplo de uso:

# Crear animales
leon = Animal("León", "Panthera leo", 5, "Sabana africana")
elefante = Animal("Elefante", "Loxodonta africana", 10, "Selva tropical")

# Mostrar detalles de los animales
leon.mostrar_detalles()
elefante.mostrar_detalles()

# Incrementar la edad de los animales
leon.cumplir_años()
elefante.cumplir_años()

# Cambiar el hábitat de los animales
leon.cambiar_habitat("Zoológico urbano")
elefante.cambiar_habitat("Área de conservación en África")

# Mostrar los detalles actualizados
leon.mostrar_detalles()
elefante.mostrar_detalles()
