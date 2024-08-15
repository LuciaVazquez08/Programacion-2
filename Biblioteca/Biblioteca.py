from Libro import Libro
from Miembro import Miembro
from Bibliotecario import Bibliotecario

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.empleados = []
        self.miembros = {}
    
    def agregar_libro(self, libro: Libro):
        self.catalogo[libro.id] = libro
    
    def eliminar_libro(self, libro: Libro):
        if libro.id in self.catalogo:
            del self.catalogo[libro.id]
        else:
            print("El libro no se encuentra en el catálogo.")
    
    def contratar(self, empleado: Bibliotecario):
        self.empleados.append(empleado)
    
    def agregar_miembro(self, miembro: Miembro):
        self.miembros[miembro.id_miembro] = miembro
    
    def get_catalogo(self):
        return self.catalogo
    
    def get_empleados(self):
        return self.empleados
    
    def get_miembros(self):
        return self.miembros
        
    def __str__(self):
        return f' Esta es la biblioteca, iba a salir un print horrendo asi que lo cortamos aca!'
    
    def prestar_libro(self, id_miembro: int, nombre_libro: str) -> None:
        libro_a_prestar = None
        for libro in self.catalogo.values():
            if libro.nombre == nombre_libro:
                libro_a_prestar = libro
                break
        
        if libro_a_prestar is None:
            print("El libro no se encuentra en el catálogo.")
            return
        
        if id_miembro not in self.miembros:
            print("El miembro no se encuentra registrado.")
            return
        
        miembro = self.miembros[id_miembro]
        miembro.prestar_libro(libro_a_prestar)
        print(f"El libro '{nombre_libro}' ha sido prestado al miembro con ID {id_miembro}.")


