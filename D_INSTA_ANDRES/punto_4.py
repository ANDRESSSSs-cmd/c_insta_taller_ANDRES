# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        """
        Inicializa los atributos de la habitación.
        :param numero: Número de la habitación (str).
        :param tipo: Tipo de habitación (str).
        :param precio: Precio por noche de la habitación (float).
        :param disponible: Estado de disponibilidad de la habitación (bool).
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada. No se puede reservar.")

    def liberar(self):
        """Marca la habitación como disponible."""
        if not self.disponible:
            self.disponible = True
            print(f"La habitación {self.numero} ha sido liberada y está disponible.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    def mostrar_informacion(self):
        """Imprime todos los detalles de la habitación."""
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"Detalles de la habitación {self.numero}:")
        print(f"Tipo: {self.tipo}")
        print(f"Precio por noche: ${self.precio}")
        print(f"Disponibilidad: {disponibilidad}")


# Ejemplo de uso:

# Crear habitaciones de ejemplo
habitacion1 = Habitacion("101", "Individual", 50)
habitacion2 = Habitacion("102", "Doble", 80)
habitacion3 = Habitacion("201", "Suite", 120)

# Mostrar detalles de todas las habitaciones
habitacion1.mostrar_informacion()
habitacion2.mostrar_informacion()
habitacion3.mostrar_informacion()

# Realizar algunas reservas
habitacion1.reservar()  # Reserva de la habitación 101
habitacion1.reservar()  # Intento de reservar una habitación ya ocupada

# Liberar una habitación
habitacion1.liberar()   # Liberación de la habitación 101

# Intentar liberar una habitación ya disponible
habitacion1.liberar()   # Intento de liberar una habitación ya disponible

# Mostrar detalles después de realizar reservas y liberaciones
habitacion1.mostrar_informacion()
habitacion2.mostrar_informacion()
habitacion3.mostrar_informacion()
