# Clase base TransportePublico
class TransportePublico:
    def __init__(self, tipo, capacidad):
        """
        Inicializa los atributos del transporte público.
        :param tipo: Tipo de transporte (str).
        :param capacidad: Número máximo de pasajeros (int).
        """
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        """Imprime los detalles básicos del transporte público."""
        print(f"Tipo de transporte: {self.tipo}")
        print(f"Capacidad: {self.capacidad} pasajeros")


# Clase hija Autobus
class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        """
        Inicializa los atributos del autobús, heredados de TransportePublico y adicionales.
        :param ruta: Número o nombre de la ruta del autobús (str).
        """
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir la ruta del autobús."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Ruta: {self.ruta}")


# Clase hija Tren
class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        """
        Inicializa los atributos del tren, heredados de TransportePublico y adicionales.
        :param numero_vagones: Número de vagones del tren (int).
        """
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el número de vagones."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Número de vagones: {self.numero_vagones}")


# Ejemplo de uso:

# Crear un autobús
autobus = Autobus("Autobús", 50, "Ruta 123")

# Crear un tren
tren = Tren("Tren", 200, 10)

# Mostrar la información del autobús
print("\nInformación del Autobús:")
autobus.mostrar_info()

# Mostrar la información del tren
print("\nInformación del Tren:")
tren.mostrar_info()
