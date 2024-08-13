from Libro import Libro 
from Miembro import Miembro 
from Biblioteca import Biblioteca, Bibliotecario

biblioteca = Biblioteca()
print(biblioteca)
print('')

libro1 = Libro('FantasticLand', 'Mike Bockoven', '12345-a', True)
libro2 = Libro('The Thursday Murder Club', 'Richard Oseman', '45678-b', False)
print(libro1)
print(libro2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print('')

miembro1 = Miembro('Lucia Vazquez')
miembro2 = Miembro('Victoria Vazquez')
print(miembro1)
print(miembro2)
print('')

bibliotecario = Bibliotecario('Raul', 'repositor', biblioteca)
biblioteca.contratar(bibliotecario)
print(bibliotecario)
print('')

print(biblioteca.get_catalogo)
print(biblioteca.get_empleados)
print(biblioteca.get_miembros)
print('')


print('')
print('presto el libro')
libro1.prestar()
print(libro1)
print('Trato de volver a prestarlo')
libro1.prestar()

print('')
print('Devuelvo el libro')
libro1.devolver()
print(libro1)
print('Trato de volver a devolverlo')
libro1.devolver()
