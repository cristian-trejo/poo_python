import random
import time

def ordenamiento_burbuja(lista, steps = 0):
    n = len(lista)
    steps += 1

    for i in range(n):
        for j in range(0, n - i - 1):

            steps += 1    
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return (lista, steps)


if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    start = time.time()
    (lista_ordenada, steps) = ordenamiento_burbuja(lista)
    end = time.time()
    execution_time = end - start

    print(f'{lista_ordenada}')
    print(f'Iteraciones ordenamiendo burbuja: {steps} \nTiempo de ejecucion: {execution_time}')