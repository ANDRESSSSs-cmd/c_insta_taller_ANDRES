# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado):
        """
        Inicializa los atributos del estudiante.
        :param nombre: Nombre del estudiante (str).
        :param edad: Edad del estudiante (int).
        :param grado: Grado o nivel escolar del estudiante (str).
        """
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []  # Lista para almacenar las materias inscritas

    def inscribir_materia(self, materia):
        """
        Agrega una materia a la lista de materias inscritas del estudiante.
        :param materia: Nombre de la materia a inscribir (str).
        """
        # Verifica si la materia ya está inscrita
        if materia not in self.materias:
            self.materias.append(materia)
            print(f"El estudiante '{self.nombre}' ha sido inscrito en la materia '{materia}'.")
        else:
            print(f"El estudiante '{self.nombre}' ya está inscrito en la materia '{materia}'.")

    def mostrar_materias(self):
        """Muestra todas las materias en las que el estudiante está inscrito."""
        if self.materias:
            print(f"El estudiante '{self.nombre}' está inscrito en las siguientes materias:")
            for materia in self.materias:
                print(f"- {materia}")
        else:
            print(f"El estudiante '{self.nombre}' no está inscrito en ninguna materia.")

    def actualizar_grado(self, nuevo_grado):
        """
        Cambia el grado del estudiante.
        :param nuevo_grado: El nuevo grado o nivel escolar (str).
        """
        self.grado = nuevo_grado
        print(f"El grado del estudiante '{self.nombre}' ha sido actualizado a '{self.grado}'.")


# Ejemplo de uso:

# Crear un estudiante
estudiante1 = Estudiante("Juan Pérez", 15, "9º Grado")

# Inscribir al estudiante en algunas materias
estudiante1.inscribir_materia("Matemáticas")
estudiante1.inscribir_materia("Ciencias")
estudiante1.inscribir_materia("Historia")

# Mostrar las materias inscritas
estudiante1.mostrar_materias()

# Inscribir al estudiante en una materia repetida (para ver el mensaje de control)
estudiante1.inscribir_materia("Ciencias")

# Actualizar el grado del estudiante
estudiante1.actualizar_grado("10º Grado")

# Mostrar la información actualizada
print(f"\nInformación actualizada del estudiante '{estudiante1.nombre}':")
print(f"Grado: {estudiante1.grado}")
estudiante1.mostrar_materias()
