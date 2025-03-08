import numpy as np
libros = []
# Creacion de la clase Libro.
class Libro():                                                              
  # Creacoin de los atributos.
    def __init__(self,isbn, titulo, autor,disponible= True):                  
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
    
    
        # Metodo agregar.
    def agregar():                                                            
      # Llamada para introducir los datos.
        titulo = str (input("Ingrese el título del libro: "))
        autor = str (input("Ingrese el autor del libro: "))
        isbn = str (input("Ingrese el isbn del libro: "))
        
        
        for libro in libros:
            if libro.isbn == isbn:
                print("El libro ya existe")
                return
        libro = Libro(isbn, titulo, autor)
        libros.append(libro)
        print("Libro agregado con exito.")
        
        
    
    def inicio():
        libros.append(Libro("1234", "El señor de los anillos", "J.R.R. Tolkien"))
        libros.append(Libro("5678", "Harry Potter y la piedra filosofal", "J.K. Rowling"))
        libros.append(Libro("2345", "El principito", "Antoine de Saint-Exupéry"))
        libros.append(Libro("6789", "Cien años de soledad", "Gabriel García Márquez"))
        libros.append(Libro("3456", "Don Quijote de la Mancha", "Miguel de Cervantes Saavedra"))
        libros.append(Libro("7890", "La Odisea", "Homero"))
        libros.append(Libro("4567", "La Iliada", "Homero"))
        libros.append(Libro("8901", "El retrato de Dorian Gray", "Oscar Wilde"))
        libros.append(Libro("9012", "El principito", "Antoine de Saint-Exupéry"))
        libros.append(Libro("0123", "Cien años de soledad", "Gabriel García Márquez"))
        libros.append(Libro("3457", "Don Quijote de la Mancha", "Miguel de Cervantes Saavedra"))
        libros.append(Libro("6780", "La Odisea", "Homero"))
        libros.append(Libro("4568", "La Iliada", "Homero"))
        libros.append(Libro("7891", "El retrato de Dorian Gray", "Oscar Wilde"))
        libros.append(Libro("8902", "El principito", "Antoine de Saint-Exupéry"))
        libros.append(Libro("0124", "Cien años de soledad", "Gabriel García Márquez"))
        libros.append(Libro("3458", "Don Quijote de la Mancha", "Miguel de Cervantes Saavedra"))
        libros.append(Libro("6781", "La Odisea", "Homero"))
        libros.append(Libro("4569", "La Iliada", "Homero"))
        
Libro.inicio()
while True:
    Libro.agregar()