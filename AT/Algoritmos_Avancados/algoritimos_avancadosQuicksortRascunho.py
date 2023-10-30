""" DESCRIÇÃO DO ALGORÍTIMO QuickSort com dois pivôs:
*** QuickSort com dois pivôs
>>> Objetivo : 
A ideia é que ao escolher dois pivôs, 
poderemos potencialmente diminuir o número total de comparações e interações 
necessárias para a ordenaçao da lista, melhorando a eficiência em algumas circunstâncias.

>>> O QuickSort é um algoritimo recursivo, que usa o método da divisão e conquista
Todos os elementos de menor valor ficam no início do vetor de acordo com o valor do pivô inicial (inicio) 
escolhido e todos os elementos de maior valor, de acordo com o valor do pivô inicial (inicio) ficam no fim, 
ordenando-os de maneira crescente.

>>> Complexidade:  
tem uma eficiência de O(n log n). 
No entanto, no pior caso, pode degradar para O(n^2),

"""
########################################################################################################

# Definindo uma função chamada particionar_tres que recebe um array e dois índices, 
# inicio e fim. 
# Esta função se encarregará de particionar a lista em três seções
def particionar_tres(arr, inicio, fim):

    # Se o elemento no índice inicio for maior que o elemento no índice fim, troca-os.
    if arr[inicio] > arr[fim]:
        arr[inicio], arr[fim] = arr[fim], arr[inicio]

    # Definindo dois pivôs, pivo1 e pivo2. 
    # pivo1 é o elemento no índice inicio e pivo2 é o elemento no índice fim.
    pivo1, pivo2 = arr[inicio], arr[fim]

    # Definindo três índices: menor, medio e maior. 
    # Eles ajudarão a particionar o array.
    menor = inicio + 1
    medio = inicio + 1

    # Decrementa o índice menor e troca os elementos nos índices inicio e menor.
    maior = fim - 1
    menor -= 1
    arr[inicio], arr[menor] = arr[menor], arr[inicio]
    
    # Incrementa o índice maior e troca os elementos nos índices fim e maior.
    maior += 1
    arr[fim], arr[maior] = arr[maior], arr[fim]
    
    # Retorna os índices menor e maior.
    return menor, maior

# Definindo a função principal quicksort_tres_pivos, 
# que realizará a ordenação QuickSort usando três pivôs.
def quicksort_tres_pivos(arr, inicio, fim):

    # Se o índice inicio for menor que o índice fim, 
    # continua a execução; caso contrário, termina a função.
    if inicio < fim:

        # Chama a função particionar_tres e recebe os índices dos dois pivôs.
        pivo1, pivo2 = particionar_tres(arr, inicio, fim)

        # Recursivamente ordena as três subpartes da lista: 
        # a primeira parte antes do pivo1, 
        quicksort_tres_pivos(arr, inicio, pivo1 - 1)
        # a parte entre pivo1 e pivo2, 
        quicksort_tres_pivos(arr, pivo1 + 1, pivo2 - 1)
        # e a última parte após o pivo2.
        quicksort_tres_pivos(arr, pivo2 + 1, fim)

# Função auxiliar ordenar para iniciar o processo de ordenação. 
# Começa a ordenação desde o início até o fim da lista.
def ordenar(arr):
    quicksort_tres_pivos(arr, 0, len(arr) - 1)

# Entrada de teste e execução
lista = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

# Definindo uma lista de exemplo para testar o algoritmo.
ordenar(lista)
print(lista)
