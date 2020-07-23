import random 
import time

def ordenamiento_mezcla(lista, steps = 0):
    # Si la longitud de la lista es 1 solo devuelve el valor de la lista
    if len(lista) > 1:      
        # Dividimos la lista en mitades hasta que sean de 1 elemento
        # Tiene un crecimiento logaritmico [line 7 - line 13]
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        #Comenzamos a comparar las listas
        while i < len(izquierda) and j < len(derecha):
            steps += 1
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        # Si quedo algo a la izquierda se copia
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedo algo a la derecha se copia
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return (lista, steps)



if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 20)

    start = time.time()
    (lista_ordenada, steps) = ordenamiento_mezcla(lista)
    end = time.time()
    execution_time = end - start

    print(f'{lista_ordenada}')
    print(f'Iteraciones ordenamiendo burbuja: {steps} \nTiempo de ejecucion: {execution_time}')
