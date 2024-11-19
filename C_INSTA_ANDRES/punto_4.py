# Clase base EmpleadoHospital
class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        """
        Inicializa los atributos del empleado del hospital.
        :param nombre: Nombre del empleado (str).
        :param id: Identificador único del empleado (int).
        :param departamento: Departamento en el que trabaja el empleado (str).
        :param salario_base: Salario base del empleado (float).
        """
        self.nombre = nombre                  # Nombre del empleado
        self.id = id                          # Identificador único del empleado
        self.departamento = departamento      # Departamento en el que trabaja
        self.salario_base = salario_base      # Salario base del empleado

    def mostrar_info(self):
        """Imprime los detalles del empleado del hospital."""
        print(f"\nInformación del Empleado:")
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario Base: ${self.salario_base:.2f}")


# Clase hija Medico
class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        """
        Inicializa los atributos del médico, heredados de EmpleadoHospital y adicionales.
        :param especialidad: Especialidad del médico (str).
        :param num_pacientes: Número de pacientes atendidos (int).
        """
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad    # Especialidad médica del médico
        self.num_pacientes = num_pacientes  # Número de pacientes atendidos

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir la especialidad y número de pacientes."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Especialidad: {self.especialidad}")
        print(f"Número de Pacientes Atendidos: {self.num_pacientes}")


# Clase hija Enfermero
class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        """
        Inicializa los atributos del enfermero, heredados de EmpleadoHospital y adicionales.
        :param turno: Turno en el que trabaja el enfermero (str: "mañana" o "noche").
        :param planta: Planta en el hospital donde trabaja el enfermero (int).
        """
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno                  # Turno del enfermero (mañana o noche)
        self.planta = planta                # Planta en el hospital donde trabaja

    def mostrar_info(self):
        """Sobrescribe el método mostrar_info para incluir el turno y planta."""
        super().mostrar_info()  # Llamamos al método de la clase base
        print(f"Turno: {self.turno}")
        print(f"Planta: {self.planta}")


# Ejemplo de uso:

# Crear un médico
medico1 = Medico("Dr. Juan Pérez", 1001, "Cardiología", 5000.00, "Cardiología", 200)

# Crear un enfermero
enfermero1 = Enfermero("Carlos López", 2001, "Urgencias", 2500.00, "Noche", 3)

# Mostrar la información del médico
print("\nInformación del Médico:")
medico1.mostrar_info()

# Mostrar la información del enfermero
print("\nInformación del Enfermero:")
enfermero1.mostrar_info()
