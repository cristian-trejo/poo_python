import random
import time

def busqueda_binaria(lista, comienzo, final, objetivo, steps = 0):
    steps += 1    
    # Si venimos de indices debemos restar 1 (off by one)
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:        
        return (False, steps)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:    
        return (True, steps)        
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, steps=steps)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, steps=steps)


if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano es la lista? '))
    objetivo = int(input('¿Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    start = time.time()
    (encontrado, steps) = busqueda_binaria(lista, 0, len(lista), objetivo)
    end = time.time()
    execution_time = end - start

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {steps} \nTiempo de ejecucion: {execution_time}')