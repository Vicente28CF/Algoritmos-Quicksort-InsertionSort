from mpi4py import MPI
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Inicializar el comunicador MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Lista a ordenar
arr = np.array([0, 11, 20, 3, 6, 50, 2], dtype='i')

# Calcular el tamaño de la sublista para cada proceso
local_size = len(arr) // size
remainder = len(arr) % size

# Calcular el desplazamiento para manejar los restos
sizes = np.array([local_size + 1 if i < remainder else local_size for i in range(size)], dtype='i')
displacement = np.array([0] + [sum(sizes[:i+1]) for i in range(size - 1)], dtype='i')

# Scatter la lista entre los procesos
local_arr = np.zeros(sizes[rank], dtype='i')
comm.Scatterv([arr, sizes.tolist(), displacement.tolist(), MPI.INT], local_arr, root=0)

# Ordenar localmente
insertion_sort(local_arr)

# Recopilar los resultados
sorted_arr = None
if rank == 0:
    sorted_arr = np.zeros(sum(sizes), dtype='i')
comm.Gatherv(local_arr, [sorted_arr, sizes.tolist(), displacement.tolist(), MPI.INT], root=0)

# Combinar y mostrar los resultados en el proceso raíz
if rank == 0:
    result = sorted(sum(sorted_arr.reshape(size, -1).tolist(), []))
    print("Lista ordenada:", result)
