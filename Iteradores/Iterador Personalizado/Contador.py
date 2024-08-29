class Contador:
    def __init__(self, inicio, fin):
        self.act = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.act <= self.fin:
            nro_act = self.act
            self.act += 1
        else:
            raise StopIteration
        return nro_act


contador = Contador(1, 5)
for numero in contador:
    print(numero) 

