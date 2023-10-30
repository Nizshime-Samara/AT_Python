import heapq # o módulo heapq, é utilizado para gerenciar uma fila de prioridades.

''' DESCRIÇÃO DO ALGORÍTIMO Dijkstra:
>>> Objetivo : 
O algoritmo de Dijkstra é uma técnica para encontrar o caminho mais curto em um grafo ponderado 
e direcionado. 
Ele utiliza uma abordagem gulosa, sempre escolhendo o próximo vértice mais próximo, 
e é garantido que encontra o caminho mais curto em um grafo sem arestas de valores negativos da reta,
ou seja, de peso negativo.

>>> Complexidade:
A complexidade de tempo total do algoritmo é O((V+E)logV).

V é o número de vértices.
E é o número de arestas.

*** O logaritmo, em termos simples, é o inverso da exponenciação. Se 2^3 = 8, então log2 8 = 3.
Ou seja, o Log na análise de complexidade é uma indicação de que a cada passo, 
o problema é reduzido substancialmente (por exemplo, cortado pela metade), 
em vez de apenas uma constante ou de forma linear(funçao de segundo grau linear).

'''
########################################################################################################

# A função dijkstra é definida com três parâmetros: grafo, ponto_de_partida e ponto_de_chegada.
def dijkstra(grafo, ponto_de_partida, ponto_de_chegada):
    # Inicializa as distâncias de todas as cidades com "infinito" e a cidade de início em 0.
    distancias = {}  # Um dicionário para armazenar as distâncias das cidades.
    for cidade in grafo:
        distancias[cidade] = float('inf')  # Todas as distâncias começam como infinitos.
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