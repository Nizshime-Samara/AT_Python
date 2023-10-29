import heapq

def dijkstra(grafo, ponto_de_partida, ponto_de_chegada):
    # Inicializa as distâncias de todas as cidades com "infinito" e a cidade de início em 0.
    distancias = {}  # Um dicionário para armazenar as distâncias das cidades.
    for cidade in grafo:
        distancias[cidade] = float('inf')  # Todas as distâncias começam como infinito.
    distancias[ponto_de_partida] = 0  # A cidade de início tem uma distância de 0.

    # Cria uma fila de prioridade para manter as cidades a serem visitadas.
    fila_prioridade = [(0, ponto_de_partida)]

    # Inicializa dicionário de predecessores para reconstruir o caminho mais curto.
    caminhos_anteriores = {}  # Um dicionário para rastrear quem veio antes de cada cidade.
    for cidade in grafo:
        caminhos_anteriores[cidade] = None  # Inicialmente, não sabemos quem veio antes de quem.

    while fila_prioridade:
        # Identifica a cidade mais próxima da fila.
        distancia_atual, cidade_atual = heapq.heappop(fila_prioridade)

        # Se chegar na cidade de destino, para.
        if cidade_atual == ponto_de_chegada:
            break

        # Percorre as cidades vizinhas.
        for vizinho, peso in grafo[cidade_atual]:
            distancia = distancia_atual + peso

            # Se for encontrado um caminho mais curto para um cidade vizinha, 
            # a distância e o predecessor são atualizados
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminhos_anteriores[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    # Reconstrói o caminho mais curto.
    caminho = []  # Uma lista para armazenar o caminho mais curto.
    cidade_atual = ponto_de_chegada  # Começamos do fim e retrocedemos até o início.
    while cidade_atual:
        caminho.insert(0, cidade_atual)  # Adiciona a cidade atual no início do caminho.
        cidade_atual = caminhos_anteriores[cidade_atual]  # Move para o próximo caminhos anteriores.

    return caminho

# Entrada que cria um exemplo de mapa com cidades, estradas e distâncias.
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Imprime e encontra o caminho mais curto entre duas cidades (vértices) no mapa.
cidade_inicial = 'A'
cidade_final = 'D'
resultado = dijkstra(grafo, cidade_inicial, cidade_final)
print(resultado)