# Clase base VehiculoCarreras
class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        """Muestra la información básica del vehículo de carreras."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")


# Clase hija CocheF1
class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de un coche F1."""
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")


# Clase hija MotoGP
class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de una moto MotoGP."""
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")


def main():
    # Instanciación de objetos
    coche_f1 = CocheF1("Ferrari", "SF1000", 370, "slick")
    moto_gp = MotoGP("Yamaha", "YZR-M1", 350, "Monoplaza")

    # Mostrar la información de los vehículos
    print("Información del vehículo de carreras:\n")

    # Mostrar información del coche F1
    print("Coche F1:")
    coche_f1.mostrar_info()
    print()  # Salto de línea para separar la información

    # Mostrar información de la moto GP
    print("Moto GP:")
    moto_gp.mostrar_info()


# Asegurarse de que el programa se ejecute solo si se ejecuta directamente
if __name__ == "__main__":
    main()

