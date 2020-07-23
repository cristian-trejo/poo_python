import random 
import time


def ordenamiento_insercion(lista, steps = 0):
    # Range(start, stop, step)
    for indice in range(1, len(lista)):
        print(indice)
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            steps += 1
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return (lista, steps)


if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    start = time.time()
    (lista_ordenada, steps) = ordenamiento_insercion(lista)
    end = time.time()
    execution_time = end - start

    print(f'{lista_ordenada}')
    print(f'Iteraciones ordenamiendo burbuja: {steps} \nTiempo de ejecucion: {execution_time}')
