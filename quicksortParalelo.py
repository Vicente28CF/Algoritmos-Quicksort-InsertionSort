'''se importan las librerias necesarias 
para la programacion paralela y numpy para operaciones numericas'''
from mpi4py import MPI
import numpy as np

'''implementa el algoritmo de manera recursiva,
divide el array en tres partes: elementos menores que el pivote, elementos iguales
al pivote y elementos mayores que el pivote.
Luego, aplica quicksort a las sublistas izquierda y derecha recursivamente'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

'''esta linea define una funcion que toma dos argumentos
rank, que representa el rango del proceso mpi
y size que representa el tamaño del comunicador mpi'''
def parallel_quicksort(rank, size):
    n = 100 
#!esta variable se utilizaa para almacenar el array no ordenado
    unsorted = None 
#!se verifica si el proceso actual tiene un rango de 0.
#!si es asi, significa que es el proceso principal y genera
#!un array no ordenado de tamaño n
    if rank == 0:
        unsorted = np.random.randint(0, 100, size=n)
        print("Unsorted array:", unsorted)  # Imprime la lista no ordenada
#!se utiliza bcast de mpi para transmitir el array no ordenado 
#!desde el proceso con rango 0 a todos los otros procesos en el comunicador mpi
    data = MPI.COMM_WORLD.bcast(unsorted, root=0)
#!se calcula el tamaño local del array que cada proceso debe manejar, dividiendo
    local_n = n // size
#!cada proceso selecciona su parte local del array no ordenado utilizando su rango
#! y el tamaño local, calculado anteriormente
    data = data[rank * local_n:(rank + 1) * local_n]
#!cada proceso ordena su parte local del array utilizando la funcion quicksort
    local_sorted = quicksort(data)
#!los resultados ordenados localmente de todos los procesos se recopilan en el proceso con rango
    gathered_data = MPI.COMM_WORLD.gather(local_sorted, root=0)
#!finalmente el proceso con rango 0 reune los resultados ordenados de todos los procesos,
#! los concatena y los imprime como el array ordenado completo
    if rank == 0:
        result = []
        for sublist in gathered_data:
            result += sublist
        print("Sorted array: ", quicksort(result))

if __name__ == "__main__":
    rank = MPI.COMM_WORLD.Get_rank()
    size = MPI.COMM_WORLD.Get_size()
    parallel_quicksort(rank, size)
