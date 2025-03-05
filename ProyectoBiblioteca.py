# Sistema de gestion de Biblioteca

class Libro:
    def __init__(self,titulo, autor, isbn, disponible=True):
        
        # Atributos de la clase libro.
        
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        
        
    # Llamada a titulo.
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def get_titulo(self):
        return self.titulo
    
    
    # LLamada a autor.
    
    def set_autor(self, autor):
        self.autor = autor
    
    def get_autor(self):
        return self.autor
    
    # Llamada a isbn.
    
    def set_isbn(self, isbn):
        self.isbn = isbn
    
    def get_isbn(self):
        return self.isbn
    
    # Llamada disponible.
    
    def set_disponible(self, disponible):
        self.disponible = disponible
    
    def get_disponible(self):
        return self.disponible 

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}"

# Agregar libro.
def agregar():
    titulo = input("Introduce el titulo del libro: ")  # Introduce el nombre del libro nuevo
    autor = input("Introduce el autor del libro: ")    # Introduce el autor del libro nuevo
    isbn = input("Introduce el ISBN: ")                # Introduce el isbn del libro nuevo
    disponible = True                                  # Introduce por defecto que esta disponible
    libro = Libro (titulo, autor,isbn,disponible)
    return libro

# Prestar libro.
def prestar():
    isbn = input("Introduce el ISBN del libro que desea retirar: ")
    isbn =Libro(isbn)





# Lista de libros
libros = ([])

# Agregar un libro a la lista
libro = agregar()
libros.append(libro)
libro = agregar()
libros.append(libro)


# Imprimir la lista de libros
for libro in libros:
    print(libro)