class Factura:
    def __init__(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = 0.0
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        # Se calcula el costo total del item
        total_item = cantidad * precio_unitario
        # Se agrega el item a la lista de items
        self.items.append({
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": total_item
        })
        # Se actualiza el monto total de la factura
        self.monto_total += total_item

    def mostrar_detalles(self):
        # Mostrar detalles de la factura
        print(f"Factura N°: {self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print("Detalles de la factura:")
        for item in self.items:
            print(f"  - {item['descripcion']}: {item['cantidad']} x {item['precio_unitario']} = {item['total']}")
        print(f"Monto total: {self.monto_total:.2f}")

    def aplicar_descuento(self, porcentaje):
        # Aplicar descuento sobre el monto total
        descuento = (self.monto_total * porcentaje) / 100
        self.monto_total -= descuento
        print(f"Descuento aplicado: {descuento:.2f}")
        print(f"Nuevo monto total con descuento: {self.monto_total:.2f}")

# Ejemplo de uso
factura = Factura(123, "Juan Pérez", "2024-11-18")
factura.agregar_item("Producto A", 2, 150)
factura.agregar_item("Servicio B", 1, 200)
factura.mostrar_detalles()
factura.aplicar_descuento(10)  # Aplicamos un 10% de descuento
factura.mostrar_detalles()
