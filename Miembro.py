from Libro import Libro

class Miembro:
    _ids_existentes = 0  

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.id_miembro = self.asignar_id()
        self.libros_prestados: list[Libro] = []

    def asignar_id(self) -> int:
        id_actual = Miembro._ids_existentes
        Miembro._ids_existentes += 1
        return id_actual
    
    def __str__(self):
        return f'Nombre: {self.nombre}, id: {self.id_miembro}, Libros en su posecion: {self.libros_prestados}'
    
    def prestar_libro(self, libro: Libro) -> None:
        if libro.check_disponibilidad():
            self.libros_prestados.append(Libro)
            libro.disponible = False
        else:
            print('No se puede prestar el libro porqeu no esat disponible')
    
    def devolver_libro(self, libro: Libro) -> None:
        if libro in libros_prestados:
            if not libro.disponible:
                libros_prestados.remove(libro)
                libro.disponible = True
            else:
                print('Ese libro esta disponible, te andaste una en algun lado')
        else:
            print('No se puede devolver el libro porque no lo tenemos')

