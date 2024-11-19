import math


# Clase base Figura3D
class Figura3D:
    def __init__(self):
        pass

    def calcular_volumen(self):
        """Método para calcular el volumen, no implementado"""
        print("Método no implementado")


# Clase hija Cubo
class Cubo(Figura3D):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self):
        """Implementa el cálculo del volumen para un cubo (lado^3)."""
        volumen = self.lado ** 3
        print(f"Volumen del cubo: {volumen} unidades cúbicas.")


# Clase hija Esfera
class Esfera(Figura3D):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        """Implementa el cálculo del volumen para una esfera (4/3 * pi * radio^3)."""
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        print(f"Volumen de la esfera: {volumen:.2f} unidades cúbicas.")


# Programa principal
def main():
    # Instanciación de objetos
    cubo = Cubo(3)  # Un cubo con lado de 3 unidades
    esfera = Esfera(4)  # Una esfera con radio de 4 unidades

    # Calcular y mostrar el volumen de las figuras
    print("Cálculo de volúmenes:")
    cubo.calcular_volumen()
    esfera.calcular_volumen()


if __name__ == "__main__":
    main()
