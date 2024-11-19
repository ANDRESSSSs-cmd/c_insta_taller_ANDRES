# Clase base VehiculoCarreras
class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        """
        Inicializa los atributos del vehículo de carreras.
        :param marca: Marca del vehículo (str).
        :param modelo: Modelo del vehículo (str).
        :param velocidad_maxima: Velocidad máxima del vehículo (int).
        """
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        """Imprime los detalles básicos del vehículo."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")


# Clase hija CocheF1
class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        """
        Inicializa los atributos del coche de F1, heredados de VehiculoCarreras y adicionales.
        :param tipo_neumaticos: Tipo de neumáticos (str).
        """
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el tipo de neumáticos."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")


# Clase hija MotoGP
class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        """
        Inicializa los atributos de la moto de MotoGP, heredados de VehiculoCarreras y adicionales.
        :param tipo_carenado: Tipo de carenado de la moto (str).
        """
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el tipo de carenado."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Tipo de Carenado: {self.tipo_carenado}")


# Ejemplo de uso:

# Crear un coche de F1
coche_f1 = CocheF1("Ferrari", "F1-2022", 350, "Slick")

# Crear una moto de MotoGP
moto_gp = MotoGP("Yamaha", "YZF-R1", 300, "Integral")

# Mostrar la información del coche de F1
print("\nInformación del Coche de F1:")
coche_f1.mostrar_info()

# Mostrar la información de la moto de MotoGP
print("\nInformación de la MotoGP:")
moto_gp.mostrar_info()
