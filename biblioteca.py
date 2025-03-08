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
            
# Se crea una variable para meter el constructor.
   
# Introduce los datos guardados en la variable libro a la lista libros.
    
    
# Metodo prestar.
    def prestar():
        # Peticion del libro a prestar y se guarda en una variable (isbn).
        isbn = input("Ingrese el isbn del libro que desea prestar: ")
        # Se crea una varible y se le da un valor para que sea booleana.
        encontrado = False
        # Se crea un bucle para buscar si esta el isbn
        for libro in libros:
            if libro.isbn == isbn:
                # Cuando encuentra el isbn cambia la variable encontrado
                encontrado = True
                if libro.disponible:
                    # Cuando lo encuentra cambia el valor de la cadena y pone que no esta disponible
                    libro.disponible = False
                    print(f"El Libro {libro.titulo} ha sido prestado exitosamente.")
                    return
                else:
                    # Si no esta disponible el libro avisa con una respuesta por pantalla.
                    print("El Libro no está disponible en este momento.")
                    return
          
        if not encontrado:
            # Si no esta el isbn en la lista da un mensaje de error.
            print("El Libro no se encuentra en la biblioteca.")

    # Metodo devolver
    def devolver():
        # Peticion de el libro que se va a devolver
        isbn = input("\n Ingrese el isbn del libro que desea devolver: ")
        encontradoD = True
        # Se crea un bucle para saber si esta en la lista.
        for libro in libros:
          if libro.isbn == isbn:
              # Cuando encuentra el isbn cambia la variable encontrado
              encontradoD = True
              if not libro.disponible:
                # Cuando lo encuentra cambia el valor de la cadena y pone que esta disponible
                libro.disponible = True
                print(f"El Libro {libro.titulo} ha sido prestado exitosamente.")
                return
              else:
                # Si no esta disponible el libro avisa con una respuesta por pantalla.
                print("El Libro no está disponible en este momento.")
                return
      
        if encontradoD:
        # Si no esta el isbn en la lista da un mensaje de error.
          print("El Libro no se encuentra en la biblioteca.")


    # Metodo mostrar
    def mostrar():
      # Se crea un bucle para saber si esta en la lista libros.
      for libro in libros:
        # Hace preguntas para saber si esta el libro
        if isinstance(libro, Libro):
            if libro.disponible == True:
              # Si se encuentra disponible muestra la variable "si" y la escribe.
              disponible = "Sí"
              print(f"-{libro.titulo} ({libro.autor}) -isbn: {libro.isbn} -Disponible: {disponible}\n")
            else:
              # Si no esta disponible el isbn guada en la variable "disponible" no y lo muestra
              disponible = "No"
              print(f"-{libro.titulo} ({libro.autor}) -isbn: {libro.isbn} -Disponible: {disponible}\n")
      
    # Metodo buscar.
    def buscar():
      # Se pregunta que isbn quiere buscar.
      isbn = input("Ingrese el isbn del libro que desea buscar: ")
      # Se crea un bucle para buscar si esta disponible.
      for Libro in libros:
        # Se guarda en una varible si esta disponible.
        disponible = Libro.disponible
        # Consulta si esta disponible en la lista
        if Libro.isbn == isbn:
          # Si la encuentra verifica si esta sisponible
            if disponible:
              # Cambia la variable disponible para poder escribir la disponibilidada y no de True.
              disponible = "Sí"
              print(f"\n El Libro con el isbn {isbn} ha sido encontrado, los datos son los siguientes:")
              print(f"\n isbn: {Libro.isbn}\n Título: {Libro.titulo}\n Autor: {Libro.autor}\n Disponible: {disponible}")
              break
      else:
        # Si no lo encuentra manda un mensaje.
        print("El Libro no ha sido encontrado.")
        
      
      
  
# Se crea una una lista para poder guardar los libros en la lista
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
      
    
# Se llama al metodo inicio para que cree una lista de libros.
Libro.inicio()
# Se crea un bucle infinito.
while True:
  # Se muestran las opciones del programa
  print("\n------BIBLIOTECA VITUAL------")
  print("\n1. Agregar Libro")
  print("2. Mostrar Libros")
  print("3. Prestar Libro")
  print("4. Devolver Libro")
  print("5. Buscar Libro")
  print("6. Salir")
  entrada = input("Ingrese una opción de la (1-6): ")
  print("\n")
  # Se selecciona la opcion y lanza el metodo elejido.
  if entrada == "1":
    Libro.agregar()
  elif entrada == "2":
    Libro.mostrar()
  elif entrada == "3":
    Libro.prestar()
  elif entrada == "4":
    Libro.devolver()
  elif entrada == "5":
    Libro.buscar()
  elif entrada == "6":
    # En esta opcion, muetra un mensaje de despedida y cierra el programa con un break
    print("Esta saliendo de la aplicación, gracias por usar nuestros productos.")
    break
  else:
    # Si la opcion no es ninguna de las anteriores muestra un mensaje y vuelve al programa.
    print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
  exit()