# Clase base EmpleadoHospital
class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        """Método para mostrar la información del empleado."""
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario Base: ${self.salario_base}")


# Clase hija Medico
class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        """Sobrescribe el método para incluir información adicional del médico."""
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")
        print(f"Número de Pacientes Atendidos: {self.num_pacientes}")


# Clase hija Enfermero
class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        """Sobrescribe el método para incluir información adicional del enfermero."""
        super().mostrar_info()
        print(f"Turno: {self.turno}")
        print(f"Planta: {self.planta}")


# Programa principal
def main():
    # Instanciación de objetos de tipo Medico
    medico1 = Medico("Dr. Santiago", "M001", "Cardiología", 45000, "Cardiología", 150)
    medico2 = Medico("Dra. Laura", "M002", "Neurología", 48000, "Neurología", 200)

    # Instanciación de objetos de tipo Enfermero
    enfermero1 = Enfermero("Cristiano", "E001", "Urgencias", 30000, "Noche", 3)
    enfermero2 = Enfermero("Neymar", "E002", "Pediatría", 32000, "Mañana", 2)

    # Mostrar la información de los empleados
    print("Información de los empleados:\n")

    # Mostrar información de los médicos
    print("Médicos:")
    medico1.mostrar_info()
    print()  # Salto de línea para mejorar la legibilidad
    medico2.mostrar_info()
    print("\n")

    # Mostrar información de los enfermeros
    print("Enfermeros:")
    enfermero1.mostrar_info()
    print()
    enfermero2.mostrar_info()


if __name__ == "__main__":
    main()
