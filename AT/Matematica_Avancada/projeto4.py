def conta_ocorrencias_recursivo(V, D, index=0):
    # Caso base: se o índice é igual ao tamanho do vetor, retornar 0
    if index == len(V):
        return 0
    
    # Verificação se o elemento atual é igual a D
    if V[index] == D:
        return 1 + conta_ocorrencias_recursivo(V, D, index + 1)
    else:
        return conta_ocorrencias_recursivo(V, D, index + 1)
def conta_ocorrencias_iterativo(V, D):
    count = 0
    for elemento in V:
        if elemento == D:
            count += 1
    return count
V = [1, 2, 3, 2, 4, 2, 5]
D = 2

# Uso da função recursiva
print(conta_ocorrencias_recursivo(V, D))  # Output previsto: 3

# Uso da função iterativa
print(conta_ocorrencias_iterativo(V, D))  # Output previsto: 3
