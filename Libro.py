class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def get_titulo(self) -> str:
        return self.titulo
    
    def get_autor(self) -> str:
        return self.autor
    
    def get_isbn(self) -> str:
        return self.isbn
    
    def check_disponibilidad(self) -> bool:
        return self.disponible
    
    def __str__(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {"Sí" if self.disponible else "No"}'
    
    def prestar(self) -> None:
        if self.disponible:
            self.disponible = False
        else:
            print('El libro no puede prestarse porque no esta disponible')

    def devolver(self) -> None:
        if not self.disponible:
            self.disponible = True
        else:
            print('No se puede devolver un libro que no estaba prestado')
