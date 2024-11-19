# Clase base TransportePublico
class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        """Muestra la información básica del transporte público."""
        print(f"Tipo de Transporte: {self.tipo}")
        print(f"Capacidad: {self.capacidad} pasajeros")


# Clase derivada Autobus
class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de un autobús."""
        super().mostrar_info()
        print(f"Ruta: {self.ruta}")


# Clase derivada Tren
class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de un tren."""
        super().mostrar_info()
        print(f"Número de Vagones: {self.numero_vagones}")


# Programa principal
def main():
    # Instanciación de objetos
    autobus1 = Autobus("Autobús", 50, "Ruta 25")
    tren1 = Tren("Tren", 300, 10)

    # Mostrar la información de los transportes
    print("Información de los transportes públicos:\n")

    # Mostrar información del autobús
    print("Autobús:")
    autobus1.mostrar_info()
    print()  # Salto de línea para separar la información

    # Mostrar información del tren
    print("Tren:")
    tren1.mostrar_info()


if __name__ == "__main__":
    main()
