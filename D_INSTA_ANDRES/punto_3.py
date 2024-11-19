from datetime import datetime

# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        """
        Inicializa los atributos del vehículo.
        :param marca: La marca del vehículo (str).
        :param modelo: El modelo del vehículo (str).
        :param año: El año de fabricación del vehículo (int).
        :param kilometraje: El kilometraje inicial del vehículo (int).
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, kilometros):
        """
        Incrementa el kilometraje del vehículo al conducir.
        :param kilometros: Número de kilómetros recorridos (int).
        """
        self.kilometraje += kilometros
        print(f"El vehículo ha sido conducido por {kilometros} km.")

    def mostrar_detalles(self):
        """Imprime todos los detalles del vehículo."""
        print(f"Detalles del Vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje} km")

    def es_vehiculo_antiguo(self):
        """
        Devuelve True si el vehículo tiene más de 20 años.
        """
        año_actual = datetime.now().year  # Obtener el año actual
        if año_actual - self.año > 20:
            return True
        else:
            return False


# Ejemplo de uso:

# Crear un vehículo
vehiculo1 = Vehiculo("Toyota", "Corolla", 2000, 150000)

# Mostrar detalles del vehículo
vehiculo1.mostrar_detalles()

# Conducir el vehículo por 100 km
vehiculo1.conducir(100)

# Mostrar los detalles después de conducir
vehiculo1.mostrar_detalles()

# Verificar si el vehículo es antiguo
if vehiculo1.es_vehiculo_antiguo():
    print(f"El vehículo {vehiculo1.marca} {vehiculo1.modelo} es antiguo.")
else:
    print(f"El vehículo {vehiculo1.marca} {vehiculo1.modelo} no es antiguo.")
