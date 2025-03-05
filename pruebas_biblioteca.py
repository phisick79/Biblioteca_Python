import random
from biblioteca_deepseek import Libro, validar_isbn

def main():
    biblioteca = []  # Lista para almacenar los libros
    errores = []  # Lista para almacenar errores detectados

    # Lista de títulos y autores para pruebas automáticas
    titulos = ["El Quijote", "1984", "Cien años de soledad", "Don Quijote", "La Odisea"]
    autores = ["Cervantes", "George Orwell", "Gabriel García Márquez", "Homero", "Miguel de Cervantes"]

    # Bucle para simular 100 interacciones
    for i in range(100):
        print(f"\n--- Iteración {i + 1} ---")
        # Selecciona una opción aleatoria entre 1 y 5
        opcion = str(random.randint(1, 5))

        if opcion == "1":  # Agregar libro
            titulo = random.choice(titulos)
            autor = random.choice(autores)
            isbn = str(random.randint(1000, 9999))  # ISBN aleatorio de 4 dígitos
            print(f"Intentando agregar libro: {titulo} ({autor}) - ISBN: {isbn}")
            # Verifica si el ISBN ya existe antes de agregar el libro
            if validar_isbn(biblioteca, isbn):
                errores.append(f"Error en iteración {i + 1}: ISBN {isbn} ya existe.")
                print(f"Error: Ya existe un libro con el ISBN {isbn}.")
            else:
                nuevo_libro = Libro(titulo, autor, isbn)
                nuevo_libro.agregar(biblioteca)

        elif opcion == "2":  # Prestar libro
            if biblioteca:  # Solo prestar si hay libros en la biblioteca
                libro = random.choice(biblioteca)
                print(f"Intentando prestar libro con ISBN: {libro.isbn}")
                if not libro.disponible:
                    errores.append(f"Error en iteración {i + 1}: Libro con ISBN {libro.isbn} ya estaba prestado.")
                libro.prestar()
            else:
                errores.append(f"Error en iteración {i + 1}: No hay libros para prestar.")
                print("No hay libros en la biblioteca para prestar.")

        elif opcion == "3":  # Devolver libro
            if biblioteca:  # Solo devolver si hay libros en la biblioteca
                libro = random.choice(biblioteca)
                print(f"Intentando devolver libro con ISBN: {libro.isbn}")
                if libro.disponible:
                    errores.append(f"Error en iteración {i + 1}: Libro con ISBN {libro.isbn} ya estaba disponible.")
                libro.devolver()
            else:
                errores.append(f"Error en iteración {i + 1}: No hay libros para devolver.")
                print("No hay libros en la biblioteca para devolver.")

        elif opcion == "4":  # Mostrar todos los libros
            print("Mostrando todos los libros:")
            if not biblioteca:
                print("No hay libros en la biblioteca.")
            else:
                for libro in biblioteca:
                    libro.mostrar()

        elif opcion == "5":  # Buscar libro por ISBN
            if biblioteca:  # Solo buscar si hay libros en la biblioteca
                libro = random.choice(biblioteca)
                isbn = libro.isbn
                print(f"Buscando libro con ISBN: {isbn}")
                encontrado = False
                for libro in biblioteca:
                    if libro.buscar(isbn):
                        encontrado = True
                        break
                if not encontrado:
                    errores.append(f"Error en iteración {i + 1}: Libro con ISBN {isbn} no encontrado.")
                    print(f"No se encontró ningún libro con el ISBN {isbn}.")
            else:
                errores.append(f"Error en iteración {i + 1}: No hay libros para buscar.")
                print("No hay libros en la biblioteca para buscar.")

    # Mostrar el estado final de la biblioteca
    print("\n--- Estado final de la biblioteca ---")
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            libro.mostrar()

    # Mostrar errores detectados
    if errores:
        print("\n--- Errores detectados ---")
        for error in errores:
            print(error)
    else:
        print("\nNo se detectaron errores durante las pruebas.")


# Ejecutar el programa
if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Biblioteca (Pruebas Automáticas)")
    main()