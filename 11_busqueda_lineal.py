import random
import time

def busqueda_lineal(lista, objetivo, steps = 0):    
    match = False    

    for elemento in lista:  # O(n)
        steps += 1
        if elemento == objetivo:
            match = True            
            break
    
    return (match, steps)


if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano sera la lista? '))
    objetivo = int(input('¿Que numero quieres encontrar?' ))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    start = time.time()
    (encontrado, steps) = busqueda_lineal(lista, objetivo)
    end = time.time()
    execution_time = end - start

    print(lista)
    # Operadores ternarios -> if else en una sola linea
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda lineal: {steps} \nTiempo de ejecucion: {execution_time}')