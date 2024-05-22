def quicksort(array, low=0, high=None):
  """
  Ordena un array usando el algoritmo Quicksort.

  Args:
    array: El array a ordenar.
    low: El índice inicial del subarray a ordenar (por defecto 0).
    high: El índice final del subarray a ordenar (por defecto, la longitud del array - 1).

  Returns:
    El array ordenado.
  """

  if high is None:
    high = len(array) - 1

#! si el indice inicial low es menor que el indice 
#!  final high entonces el 
#!  array aun no esta completamente ordenado
  if low < high: 
    pivot = partition(array, low, high)
    quicksort(array, low, pivot - 1)
    quicksort(array, pivot + 1, high)
#!se elige un pivote usando la función partition y se,
#!divide el array en dos subarrays alrededor del pivote.
#!luego se aplica el algoritmo quicksort recursivamente a ambos subarrays.
  return array

def partition(array, low, high):
  """
  Particiona un subarray en dos subarrays alrededor de un pivote.

  Args:
    array: El array a particionar.
    low: El índice inicial del subarray.
    high: El índice final del subarray.

  Returns:
    El índice del pivote en la posición final correcta.
  """
#!se elige el pivote como el ultimo elemento del subarray 
  pivot = array[high]
  i = low - 1 #!se inicializa un indice i que se utiliza 
  #!para mantener el indice del ultimo elemento menor que el pivote

#!este bucle recorre el subarray desde el low hasta high -1
#!si encuentra un elemento que es menor o igual al pivote, intercambia
#!ese elemento con el elemento en la posicion i y luego se incrementa i.
#! esto asegura que los elementos menores que el pivote esten a la izquierda de i.
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
#!finalmente se intercambia el pivote con el elemento en la posicion i +1
#!lo que coloca al pivote en su posicion correcta en el array ordenado.
#!se devuelve i + 1 que es el indice del pivote en su posicion final correcta.
  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1
# Ejemplo de uso

array = [5, 2, 4, 1, 3]
print("Array original:", array)

array = quicksort(array)
print("Array ordenado:", array)
