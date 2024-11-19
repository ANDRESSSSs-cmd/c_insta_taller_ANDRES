# Clase base ProductoElectronico
class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        """
        Inicializa los atributos del producto electrónico.
        :param nombre: Nombre del dispositivo (str).
        :param precio: Precio del dispositivo en dólares (float).
        :param marca: Marca del dispositivo (str).
        """
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        """Imprime los detalles básicos del producto."""
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Marca: {self.marca}")


# Clase hija TelefonoMovil
class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        """
        Inicializa los atributos del teléfono móvil, heredados de ProductoElectronico y adicionales.
        :param capacidad_bateria: Capacidad de la batería en mAh (int).
        """
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir la capacidad de la batería."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Capacidad de Batería: {self.capacidad_bateria} mAh")


# Clase hija Laptop
class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        """
        Inicializa los atributos de la laptop, heredados de ProductoElectronico y adicionales.
        :param tamano_pantalla: Tamaño de la pantalla en pulgadas (float).
        """
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el tamaño de la pantalla."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Tamaño de Pantalla: {self.tamano_pantalla} pulgadas")


# Ejemplo de uso:

# Crear un teléfono móvil
telefono = TelefonoMovil("iPhone 14", 999.99, "Apple", 3500)

# Crear una laptop
laptop = Laptop("MacBook Pro", 2399.99, "Apple", 16)

# Mostrar la información del teléfono móvil
print("\nInformación del Teléfono Móvil:")
telefono.mostrar_info()

# Mostrar la información de la laptop
print("\nInformación de la Laptop:")
laptop.mostrar_info()
