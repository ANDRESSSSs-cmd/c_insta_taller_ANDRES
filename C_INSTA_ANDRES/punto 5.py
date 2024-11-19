import math

# Clase base Figura3D
class Figura3D:
    def calcular_volumen(self):
        """Método que se supone debe ser implementado en las clases hijas"""
        print("Método no implementado")

# Clase hija Cubo
class Cubo(Figura3D):
    def __init__(self, lado):
        """
        Inicializa el atributo lado del cubo.
        :param lado: Longitud de un lado del cubo.
        """
        self.lado = lado

    def calcular_volumen(self):
        """Sobrescribe el método calcular_volumen para calcular el volumen del cubo."""
        volumen = self.lado ** 3
        return volumen

# Clase hija Esfera
class Esfera(Figura3D):
    def __init__(self, radio):
        """
        Inicializa el atributo radio de la esfera.
        :param radio: Radio de la esfera.
        """
        self.radio = radio

    def calcular_volumen(self):
        """Sobrescribe el método calcular_volumen para calcular el volumen de la esfera."""
        volumen = (4/3) * math.pi * self.radio ** 3
        return volumen


# Ejemplo de uso:

# Crear un cubo con lado 4
cubo = Cubo(4)
print(f"Volumen del cubo: {cubo.calcular_volumen()} unidades cúbicas")

# Crear una esfera con radio 3
esfera = Esfera(3)
print(f"Volumen de la esfera: {esfera.calcular_volumen():.2f} unidades cúbicas")
