from Libro import Libro
from Miembro import Miembro

class Bibliotecario(Miembro):
    def __init__(self, nombre: str, puesto: str, lugar_de_empleo):
        super().__init__(nombre)
        self.puesto = puesto
        self.lugar_de_empleo = lugar_de_empleo
        self.libros_prestados = []

    def agregar_libro(self, libro: Libro) -> None:
        self.lugar_de_empleo.catalogo.append(libro)
        print(f'El libro {libro.titulo} ha sido agregado al catálogo de la biblioteca.')


    def eliminar_libro(self, libro: Libro) -> None:
        if libro in self.lugar_de_empleo.catalogo:
            self.lugar_de_empleo.catalogo.remove(libro)
            print(f'El libro {libro.titulo} ha sido eliminado del catálogo de la biblioteca.')
        else:
            print('El libro no se encuentra en el catálogo.')
    
    def __str__(self):
        return f'Nombre: {self.nombre}, puesto: {self.puesto}, lugar de trabajo: {self.lugar_de_empleo}'