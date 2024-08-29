def fibonacci(n):
    a, b = 0, 1
    contador = 0
    while a < n:
        yield a
        a, b = b, a + b
        contador += 1

fib = fibonacci(9)
for numero in fib:
    print(numero)

def fibonacciOther(n):
    a, b = 0, 1
    contador = 0
    while contador < n:
        yield a
        a, b = b, a + b
        contador += 1

fib = fibonacciOther(9)
for numero in fib:
    print(numero)


        
