def fibonacci_hasta(n):
    a, b = 0, 1
    contador = 0
    while a < n:
        yield a
        a, b = b, a + b
        contador += 1

fib = fibonacci_hasta(1513)
for numero in fib:
    print(numero)

def fibonacci_cantidad(n):
    a, b = 0, 1
    contador = 0
    while contador < n:
        yield a
        a, b = b, a + b
        contador += 1

fib = fibonacci_cantidad(1565)
for numero in fib:
    print(numero)


        
