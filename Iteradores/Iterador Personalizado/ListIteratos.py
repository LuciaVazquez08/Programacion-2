class ListIterator:
    def __init__(self, lista):
        self.lista = lista
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lista):
            elemento = self.lista[self.index]
            self.index += 1
            return elemento
        else:
            raise StopIteration

class ListIteratorPotencia:
    def __init__(self, lista):
        self.lista = lista
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lista):
            elemento = self.lista[self.index]
            self.index += 1
            return elemento ** 2
        else:
            raise StopIteration
        
iterador = ListIterator([0,1,2,3,4,5])
for num in iterador:
    print(num**2)

iterador = ListIteratorPotencia([0,1,2,3,4,5])
for num in iterador:
    print(num)