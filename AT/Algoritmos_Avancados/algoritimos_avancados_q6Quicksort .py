def particionar_tres(arr, inicio, fim):
    if arr[inicio] > arr[fim]:
        arr[inicio], arr[fim] = arr[fim], arr[inicio]

    pivo1, pivo2 = arr[inicio], arr[fim]
    menor = inicio + 1
    medio = inicio + 1

    maior = fim - 1
    menor -= 1
    arr[inicio], arr[menor] = arr[menor], arr[inicio]

    maior += 1
    arr[fim], arr[maior] = arr[maior], arr[fim]

    return menor, maior

def quicksort_tres_pivos(arr, inicio, fim):
    if inicio < fim:

        pivo1, pivo2 = particionar_tres(arr, inicio, fim)
        quicksort_tres_pivos(arr, inicio, pivo1 - 1)
        quicksort_tres_pivos(arr, pivo1 + 1, pivo2 - 1)
        quicksort_tres_pivos(arr, pivo2 + 1, fim)

def ordenar(arr):
    quicksort_tres_pivos(arr, 0, len(arr) - 1)

lista = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
ordenar(lista)
print(lista)
