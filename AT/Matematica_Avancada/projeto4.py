'''
A função é planejada para tratar do caso geral(contar o número de ocorrências de um determinado valor D em um vetor V), 
verificando o valor atual do vetor e se necessário somando antes de fazer a chamada recursiva.
Esta função usa a recursão como sua abordagem principal, onde a ideia por trás da recursão é dividir o 
problema em subproblemas menores, resolvê-los individualmente e combinar seus resultados para obter a solução final 
A classificação correta desse problema é P (Problemas Polinomiais) .
Complexidade  O(n). 
'''
def conta_ocorrencias_recursivo(V, D, index=0):
    # Caso base: se o índice é igual ao tamanho do vetor, retornar 0
    if index == len(V):
        return 0
    
    # Verificação se o elemento atual é igual a D
    if V[index] == D:
        return 1 + conta_ocorrencias_recursivo(V, D, index + 1)
    else:
        return conta_ocorrencias_recursivo(V, D, index + 1)
    
'''
A função é planejada para tratar do caso geral(contar o número de ocorrências de um determinado valor D em um vetor V), 
a função iterativa conta_ocorrencias_iterativo usa uma estrutura de repetição 
for para percorrer todo o vetor V.
A classificação correta desse problema é P (Problemas Polinomiais) 
Complexidade  O(n). 
'''
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
