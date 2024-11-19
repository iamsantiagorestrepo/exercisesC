class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El material '{self.titulo}' ha sido prestado.")
        else:
            print(f"El material '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El material '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El material '{self.titulo}' ya está disponible.")

    def mostrar_informacion(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nCódigo: {self.codigo}\nDisponibilidad: {disponibilidad}")

#Clases hijas Libro y Revista
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Páginas: {self.numero_paginas}")
        print(f"Género: {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible=True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de Edición: {self.numero_edicion}")
        print(f"Fecha de Publicación: {self.fecha_publicacion}")


def main():
    # Instanciamos libros
    libro1 = Libro("El Alquimista", "Paulo Coelho", "LB001", 208, "Ficción")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "LB002", 471, "Realismo mágico")
    libro3 = Libro("1984", "George Orwell", "LB003", 328, "Distopía")

    # Instanciamos revistas
    revista1 = Revista("Wired", "Varios", "RV001", 320, "05/2023")
    revista2 = Revista("Sports Illustrated", "Varios", "RV002", 120, "10/2023")
    revista3 = Revista("Scientific American", "Varios", "RV003", 500, "01/2024")

    # Mostrar información de los libros
    print("Información de los libros:")
    libro1.mostrar_informacion()
    print()  # Salto de línea para mejorar la legibilidad
    libro2.mostrar_informacion()
    print()
    libro3.mostrar_informacion()
    print("\n")

    # Mostrar información de las revistas
    print("Información de las revistas:")
    revista1.mostrar_informacion()
    print()  # Salto de línea para mejorar la legibilidad
    revista2.mostrar_informacion()
    print()
    revista3.mostrar_informacion()
    print("\n")

    # Simulamos un préstamo y devolución de libros y revistas
    print("Préstamos y devoluciones:")

    # Préstamos y devoluciones de libros
    libro1.prestar()
    libro2.prestar()
    libro1.devolver()
    libro2.devolver()

    # Préstamos y devoluciones de revistas
    revista1.prestar()
    revista3.devolver()
    revista1.devolver()

if __name__ == "__main__":
    main()