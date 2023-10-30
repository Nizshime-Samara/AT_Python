import heapq

def dijkstra(grafo, ponto_de_partida, ponto_de_chegada):
    distancias = {}  
    for cidade in grafo:
        distancias[cidade] = float('inf')  
    distancias[ponto_de_partida] = 0  

    fila_prioridade = [(0, ponto_de_partida)]

    caminhos_anteriores = {} 
    for cidade in grafo:
        caminhos_anteriores[cidade] = None  

    while fila_prioridade:
        distancia_atual, cidade_atual = heapq.heappop(fila_prioridade)

        if cidade_atual == ponto_de_chegada:
            break

        for vizinho, peso in grafo[cidade_atual]:
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminhos_anteriores[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    caminho = []  
    cidade_atual = ponto_de_chegada  
    while cidade_atual:
        caminho.insert(0, cidade_atual)  
        cidade_atual = caminhos_anteriores[cidade_atual]  

    return caminho
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
cidade_inicial = 'A'
cidade_final = 'D'
resultado = dijkstra(grafo, cidade_inicial, cidade_final)
print(resultado)