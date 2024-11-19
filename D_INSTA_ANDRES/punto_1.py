# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa los atributos del producto.
        :param nombre: Nombre del producto (str).
        :param precio: Precio del producto en dólares (float).
        :param cantidad: Cantidad de unidades disponibles (int).
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """
        Cambia el precio del producto.
        :param nuevo_precio: El nuevo precio para el producto (float).
        """
        self.precio = nuevo_precio
        print(f"El precio de '{self.nombre}' ha sido actualizado a ${self.precio:.2f}.")

    def ajustar_inventario(self, cantidad_ajuste):
        """
        Ajusta la cantidad de unidades del producto.
        :param cantidad_ajuste: La cantidad a incrementar o disminuir (int).
                             Puede ser negativo para disminuir la cantidad.
        """
        self.cantidad += cantidad_ajuste
        if cantidad_ajuste > 0:
            print(f"Se han agregado {cantidad_ajuste} unidades de '{self.nombre}'.")
        elif cantidad_ajuste < 0:
            print(f"Se han vendido {abs(cantidad_ajuste)} unidades de '{self.nombre}'.")
        else:
            print(f"No se realizaron cambios en el inventario de '{self.nombre}'.")

    def mostrar_informacion(self):
        """Muestra los detalles completos del producto."""
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad} unidades")


# Ejemplo de uso:

# Crear un producto
producto1 = Producto("Camiseta", 19.99, 50)

# Mostrar información del producto
print("\nInformación inicial del producto:")
producto1.mostrar_informacion()

# Actualizar el precio del producto
producto1.actualizar_precio(22.99)

# Ajustar el inventario (agregar o vender unidades)
producto1.ajustar_inventario(30)  # Agregar 30 unidades
producto1.ajustar_inventario(-10)  # Vender 10 unidades

# Mostrar la información después de los cambios
print("\nInformación actualizada del producto:")
producto1.mostrar_informacion()
