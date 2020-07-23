# Ley de la suma

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n)
        print(i)

# O(n) + O(n * n) = O(n + n^2) = O(n^2)

def f(x):

    respuesta = 0

    for i in range(1000):
        respuesta += 1

    for i in range(x):
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta

# O(1000) + O(x) + O(x * x) = O(x + x^2) = O(x^2)

# Ley de la multiplicacion

def f(n):
    for i in range(n):
        
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n^2)

# Recursividad multiple

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# Crece exponencialmente porque hay dos llamadas recursivas a la funcion
# O(2**n)