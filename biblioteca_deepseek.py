# Definición de la clase Libro.
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def agregar(self, biblioteca):
        # Verifica si el ISBN ya existe en la biblioteca
        for libro in biblioteca:
            if libro.isbn == self.isbn:
                print(f"Error: Ya existe un libro con el ISBN {self.isbn}.")
                return False  # Indica que el libro no se agregó
        # Si el ISBN no existe, agrega el libro
        biblioteca.append(self)
        print(f"Libro '{self.titulo}' agregado con éxito.")
        return True  # Indica que el libro se agregó correctamente

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def mostrar(self):
        estado = "Sí" if self.disponible else "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")

    def buscar(self, isbn):
        if self.isbn == isbn:
            estado = "Sí" if self.disponible else "No"
            print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")
            return True
        return False


# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    return input("Elige una opción: ").strip()


# Función para validar si un ISBN existe en la biblioteca
def validar_isbn(biblioteca, isbn):
    for libro in biblioteca:
        if libro.isbn == isbn:
            return libro
    return None


# Programa principal
def main():
    biblioteca = []  # Lista para almacenar los libros

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Agregar libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            # Verifica si el ISBN ya existe antes de agregar el libro
            if validar_isbn(biblioteca, isbn):
                print(f"Error: Ya existe un libro con el ISBN {isbn}.")
            else:
                nuevo_libro = Libro(titulo, autor, isbn)
                nuevo_libro.agregar(biblioteca)

        elif opcion == "2":  # Prestar libro
            isbn = input("Ingresa el ISBN: ")
            libro = validar_isbn(biblioteca, isbn)
            if libro:
                libro.prestar()
            else:
                print(f"No se encontró ningún libro con el ISBN {isbn}.")

        elif opcion == "3":  # Devolver libro
            isbn = input("Ingresa el ISBN: ")
            libro = validar_isbn(biblioteca, isbn)
            if libro:
                libro.devolver()
            else:
                print(f"No se encontró ningún libro con el ISBN {isbn}.")

        elif opcion == "4":  # Mostrar todos los libros
            if not biblioteca:
                print("No hay libros en la biblioteca.")
            else:
                print("Libros en la biblioteca:")
                for libro in biblioteca:
                    libro.mostrar()

        elif opcion == "5":  # Buscar libro por ISBN
            isbn = input("Ingresa el ISBN: ")
            encontrado = False
            for libro in biblioteca:
                if libro.buscar(isbn):
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró ningún libro con el ISBN {isbn}.")

        elif opcion == "6":  # Salir del programa
            print("Saliendo del programa...")
            break

        else:  # Opción inválida
            print("Opción inválida. Por favor, elige una opción del 1 al 6.")


# Ejecutar el programa
if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    main()