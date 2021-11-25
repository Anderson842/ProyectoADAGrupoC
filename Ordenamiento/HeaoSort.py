# Reorganizamos el heap para mantener su propiedad
# n es el tamaño del heap
def heapify(arr, n, i):
    largest = i  # Inicializamos como raiz el mas grande
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    # Verificar si el hijo izquierdo es mayor que la raiz
    if l < n and arr[i] < arr[l]:
        largest = l
  
    # Verificar si el hijo derecho es mayor que la raiz
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Cambio de raiz
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest)
  
# Ordenamineto
def heapSort(arr):
    n = len(arr)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)
  
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print (arr[i]),