# Definicion de la calse Libro.
class Libro:
    def __init__(self, isbn,titulo, autor, disponible=True):
        
        # Atributos de la clase libro.
        
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        
    # Metodo agregar Biblioteca.
    def agregar(self,biblioteca):
        for libro in biblioteca:
            if libro.isbn == self.isbn:
                print(f"Error: Ya existe un libro con el ISBN {self.isbn}")
        biblioteca.append(self)
        print(f"el libro {self.titulo}, se ha agregado correctamente")
    
    # Metodo prestar libro.
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo}, ha sido prestado.")
        else:
            print(f"El libro {self.titulo}, esta prestado.")
    
    # Metodo devolver.
    def devolver(self):
        if self.disponible:
            print(f"El libro {self.titulo}, ya esta disponible.")
        else:
            self.disponible = True
            print(f"El libro {self.titulo}, ha sido devuelto con exito.")
    
    # Metodo mostrar.
    def mostrar(self):
        estado = "No"       # Guarda en la variable estado "No"
        print(f"- {self.titulo} ({self.autor})\n - ISBN: {self.isbn}\n - Disponible: {estado}")
            
    
    # Metodo buscar.
    def buscar(self,isbn):          # Busca en Libro.
        if self.isbn == isbn:       # Compara los datos que vamos a meter con los que ahi en Libros.
            if self.disponible:     # Mira si esta disponible el libro con la ISBN introducida
                estado = "Si"       # Si esta disponible crea y guarda una variable con el sring "Si"
            else:                   # si no se cumple que esta disponible.
                estado = "No"       # Guarda en la variable estado "No"
            print(f"- {self.titulo} ({self.autor})\n - ISBN: {self.isbn}\n - Disponible: {estado}")   
            return True             # Devuelve verdadero si es igual el isbn al buscado. 
        return False                # Devuelve falso si no es igual el isbn al que estabamos buscando.
    
# Funcion mostrar el menu 
def menu_principal():
    print("----Menu principal de la Biblioteca----\n")
    print("1. Agregar Libro.")
    print("2. Prestar Libro.")
    print("3. Devolver Libro.")
    print("4. Mostrar Libros.")
    print("5. Buscar por ISBN.")
    print("6. Salir del programa.")
    return input("\nIntroduce una opcion de las mostradas 1-6:")     # Cuando se llama a la funcion del menu
                                                                        # devuelve la opcion que se selecciona.
    
    
# Funcion para validar si isbn esta en la biblioteca
def validar_isbn(biblioteca, isbn):
    for libro in biblioteca:            # Crea un bucle para buscar en biblioteca y lo guarda en libro.
        if libro.isbn == isbn:          # Busca en libro que ha volcado de la lista biblioteca el isbn.
            return libro                # Devuelve la variable guardada en libro.
        
    return None                         # Si el isbn no se encuentra no devuelve nada.
    

# Programa principal.
def main():
    biblioteca = []                     # Lista donde se almacenan los libros.
    
    while True:
        seleccion = menu_principal()
        if seleccion == "1":             # Agregar libro
           titulo = input("Titulo: ")   # Guarda una entrada en una variable titulo.
           autor = input("Autor: ")     # Guarda una entrada en la variable autor.
           isbn = input("ISBN: ")       # Guarda una entrada en la variable isbn.
           nuevoLibro = Libro(titulo, autor, isbn)
           nuevoLibro.agregar(biblioteca)
       
        elif seleccion == "2":                      # Prestar libro.
            isbn = input("Ingresa el ISBN: ")       # Ingresa el isbn para prestar libro.
            libro = validar_isbn(biblioteca,isbn)   # Valida el isbn y devuelve una respuesta booleana.
            if libro:                               # Si libro es verdadero.
               libro.prestar()                      # Ejecuta prestar con el isbn
            else:                                   # Si no ahi ningun libro con el isbn introducido devuelve un comentario.
               print(f"<No ahi ningun libro con el ISBN: {isbn}.")
        
        elif seleccion == 3:                        # Devolver libro.
            isbn = input("Ingresa el ISBN: ")       # Ingresa en la variable isbn el valor introducido.
            libro = validar_isbn(biblioteca,isbn)   # Valida el isbn y devuelve una respuesta booleana.
            if libro:                               # Si libro es verdadero.
                libro.devolver()                    # Ejecuta devolver con el isbn
            else:                                   # Si no ahi ningun libro con el isbn introducido devuelve un comentario.
               print(f"<No ahi ningun libro con el ISBN: {isbn}.")
               
        elif seleccion == 4:                        # Mostrar todos los libros
            if not biblioteca:                      # Si ahi ningun libro en la biblioteca.
                print("No se ha introducido ningun libro.")
            else:                                   # Si ahi alguno.
                print("Libros en la biblioteca\n")  # Encabezado  de la biblioteca.
                for libro in biblioteca:            # Busca en biblioteca todos los datos.
                    libro.mostrar()                 # Ejecuta mostrar hasta que se acaba el string biblioteca.
        
        
        elif seleccion == 5:                        # Buscar por isbn.
            isbn = input("Ingresa el ISBN: ")       # Ingresa en la variable isbn el valor introducido.
            encontrado = False                      # Dar un valor a una variable.
            for libro in biblioteca:                # Busca en la biblioteca hasta que encuentra el isbn.
                if libro.mostrar(isbn):             # Escribe el libro
                    encontrado = True
                break
            if not encontrado:                      # Si no lo encuentra muestra un mensaje.
                print(f"No se encontro ningun libro son el ISBN: {isbn}")
        
        elif seleccion == 6:                        # Salida del programa.
            print("Eso es todo amigos.")            # Mensaje de salida
            break                                   # Salida del programa
        
        else:                                       # Si no te enteras.
            print("Mira que te he dicho que es del 1 al 6.")
            
# Ejecucion del programa.
if __name__ == "__main__":
    print("Este es el programa de gestion para bibliotecas")
    main()