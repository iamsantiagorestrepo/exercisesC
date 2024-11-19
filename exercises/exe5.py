# Clase base Mascota
class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        """Muestra la información básica de la mascota."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Especie: {self.especie}")


# Clase derivada Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de un perro."""
        super().mostrar_info()
        print(f"Raza: {self.raza}")

    def ladrar(self):
        """Imprime el sonido que hace un perro."""
        print("Guau, guau")


# Clase derivada Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def mostrar_info(self):
        """Sobrescribe el método para mostrar la información de un gato."""
        super().mostrar_info()
        print(f"Color: {self.color}")

    def maullar(self):
        """Imprime el sonido que hace un gato."""
        print("Miau")


# Programa principal
def main():
    # Instanciación de objetos
    perro1 = Perro("Max", 5, "Perro", "Labrador")
    gato1 = Gato("Luna", 3, "Gato", "Blanco")

    # Mostrar la información de las mascotas
    print("Información de las mascotas:\n")

    # Mostrar información del perro
    print("Perro:")
    perro1.mostrar_info()
    perro1.ladrar()
    print()  # Salto de línea para separar la información

    # Mostrar información del gato
    print("Gato:")
    gato1.mostrar_info()
    gato1.maullar()


if __name__ == "__main__":
    main()
