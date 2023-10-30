import random
''' DESCRIÇÃO DO ALGORÍTIMO Genético:
 >>> Objetivo:
# A lógica é criar uma população de indivíduos, avaliar sua aptidão, 
# selecionar os melhores, cruzá-los para produzir novos indivíduos e, ocasionalmente, 
# mutar alguns genes para introduzir variação genética.
#
# O processo se repete por um número definido de gerações (geracoes_max). 
# Em cada geração:
# 1 - A população é ordenada por aptidão.
# 2 - Se o melhor indivíduo alcança o objetivo, ele é armazenado em individuos_alcancaram_objetivo.
# 3 - São selecionados os melhores indivíduos da população.
# 4 - Os indivíduos selecionados são cruzados para produzir novos indivíduos.
# 5 - Alguns dos novos indivíduos sofrem mutação.
# 6 - A nova população é formada pelos melhores indivíduos da geração anterior e pelos novos indivíduos produzidos.
#
 >>> Sobre a Técnica :
# A técnica utilizada é o Algoritmo Genético, 
# que é uma técnica de busca heurística inspirada no processo de seleção natural. 
# Eles são usados para encontrar soluções aproximadas para problemas de otimização e busca.
#
 >>> Complexidade :
#  O(g *(p log p)) ou O(g *p log p) expressa que, 
# à medida que tanto o número de gerações (g) quanto o tamanho da população (p) crescem, 
# o tempo de execução do algoritmo crescerá proporcionalmente ao produto de 
# g pelo tamanho da população multiplicado pelo logaritmo do tamanho da população. 

'''
##########################################################################################

# A aptidao é o resultado da soma dos genes de cada individuo, 
# em nosso caso deve ser funcao_objetivo = 6
def calcular_aptidao(individuo):
    return sum(individuo) 

# algoritmo de ordenação dividir para conquistar.
def merge_sort(populacao):

    #Se a população tiver tamanho 1 ou menos, ela já está ordenada.
    if len(populacao) <= 1:
        return populacao

    # Divide a população em duas metades.
    meio = len(populacao) // 2
    # Ordena recursivamente ambas as metades.
    esquerda = merge_sort(populacao[:meio])
    direita = merge_sort(populacao[meio:])

    # Mescla as duas metades ordenadas, chamando a função mesclar.
    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    # Inicializa uma lista vazia result 
    result = []
    # Inicializa e dois índices para as listas esquerda e direita.
    esq_idx, dir_idx = 0, 0

    # Enquanto enquanto ambos os índices forem menores que os tamanhos de suas respectivas listas.
    while esq_idx < len(esquerda) and dir_idx < len(direita): 
        # Compara a aptidão do elemento atual da lista esquerda com a aptidão do elemento atual da lista direita.
        # Se/if a aptidão do elemento da esquerda for maior que o do elemento da direita
        if calcular_aptidao(esquerda[esq_idx]) > calcular_aptidao(direita[dir_idx]):
            # adiciona o elemento da lista esquerda à lista result.
            result.append(esquerda[esq_idx])
            # Incrementa o índice esq_idx para avançar para o próximo elemento da lista esquerda.
            esq_idx += 1

        # Se a aptidão do elemento da esquerda não for maior (ou seja, for menor ou igual)...
        else:
            # Adiciona o elemento da lista direita à lista result.
            result.append(direita[dir_idx])
            # Incrementa o índice dir_idx para avançar para o próximo elemento da lista direita.
            dir_idx += 1
    # Uma vez que o loop termina (porque um dos índices alcançou o final de sua respectiva lista), 
    # essa linha adiciona todos os elementos restantes da lista esquerda à lista result. 
    result.extend(esquerda[esq_idx:])
    result.extend(direita[dir_idx:])

    # Da mesma forma, essa linha adiciona todos os elementos restantes da lista direita à lista result.
    return result

# Retorna os tamanho_selecao primeiros indivíduos da população,
# presumindo que a população já está ordenada por aptidão.
def selecionar_melhores(populacao, tamanho_selecao):
    return populacao[:tamanho_selecao]

def realizar_crossover(individuo1, individuo2):
    # Escolhe um ponto aleatório para o crossover entre 1 e 5.
    ponto_crossover = random.randint(1, 5)

    #Cria dois filhos(filho1 e filho2) combinando partes dos pais no ponto de crossover.
    filho1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    filho2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]

    # Retorna os dois filhos.
    return filho1, filho2

def realizar_mutacao(individuo, taxa_mutacao):
    # Executa três tentativas de mutação no indivíduo.
    # Para cada tentativa, verifica se ocorrerá uma mutação (baseado na taxa_mutacao).
    for _ in range(3):
        # Se sim, escolhe um gene aleatório para mutar (invertendo seu valor de 0 para 1 ou de 1 para 0).
        # Validaçao: A função random.random() é para retornar um número decimal entre 0 e 1, 
        # isto ajudará a determinar se uma mutação deve ocorrer. 
        # Se esse número(resultado de random.random()) for menor que a taxa_mutacao fornecida, 
        # vai indicar que uma mutação deve ocorrer. 
        if random.random() < taxa_mutacao:
            # Aqui, a função escolhe um índice de gene aleatório para mutar. 
            # O índice está no intervalo de 0 a 5, o que sugere que o indivíduo tem 6 genes (índices de 0 a 5 inclusive).
            gene = random.randint(0, 5)

            # Aqui, o gene selecionado é invertido. Se o valor atual do gene for 0, ele se tornará 1 e vice-versa. 
            # Essa inversão é conseguida subtraindo o valor atual do gene de 1.
            individuo[gene] = 1 - individuo[gene]

tamanho_populacao = 4 
tamanho_apos_cruzamento = 8
tamanho_selecao = 4
geracoes_max = 8
taxa_mutacao = 0.005
funcao_objetivo = 6 

populacao = []

# Execuçao de loop da interaçao com o usuário do algorítimo 
# até atingir a qtd necessária de entrada de cada individuo e seus genes.
for individuo_index in range(tamanho_populacao):
    print(f"Digite os 6 genes (0 ou 1) para o indivíduo {individuo_index  + 1} sem espaços:")
    entrada = input("Genes: ")
    genes = [int(gene) for gene in entrada]
    if len(genes) != 6:
        print("Você deve fornecer exatamente 6 genes. Tente novamente.")
        continue
    populacao.append(genes)

individuos_que_alcancaram_objetivo = []

# Este loop irá iterar por um número definido de gerações (geracoes_max).
for geracao in range(geracoes_max):
    # Aqui, a população atual é ordenada usando o algoritmo merge_sort.
    populacao = merge_sort(populacao)

    # se o indivíduo mais apto (o primeiro da lista ordenada) atende ao critério da função objetivo = 6.
    if calcular_aptidao(populacao[0]) == funcao_objetivo:
        # Entao, ele é copiado para a lista individuos_que_alcancaram_objetivo.
        individuos_que_alcancaram_objetivo.append(populacao[0].copy())

    # Aqui, selecionar_melhores é chamada: 
    # para selecionar os tamanho_selecao indivíduos mais aptos da população e armazená-los na lista melhores.
    melhores = selecionar_melhores(populacao, tamanho_selecao)

    # Uma lista vazia chamada filhos é inicializada. 
    # Esta lista armazenará os novos indivíduos gerados pelo processo de cruzamento.
    filhos = []

    #  Enquanto o número de filhos gerados for menor que tamanho_apos_cruzamento.
    while len(filhos) < tamanho_apos_cruzamento:

        # Dois indivíduos (pai1, pai2) 
        # são selecionados aleatoriamente da lista melhores para atuarem como pais no cruzamento.
        pai1, pai2 = random.sample(melhores, 2)

        # Os dois pais selecionados serao passados como parametro para serem cruzados usando a função realizar_crossover 
        # para assim produzir dois filhos (filho1, filho2) de acordo com a taxa 0.5 de mutaçao.
        filho1, filho2 = realizar_crossover(pai1, pai2)
        realizar_mutacao(filho1, taxa_mutacao)
        realizar_mutacao(filho2, taxa_mutacao)

        # O filho1 é adicionado à lista filhos.
        filhos.append(filho1)
       
        # Se houver espaço na lista filhos, 
        # validando se len(filhos) for menor que tamanho_apos_cruzamento. 
        if len(filhos) < tamanho_apos_cruzamento:
            # Entao, o filho2 também é adicionado a lista filhos
            filhos.append(filho2)

    # a lista população para a próxima geração é formada pelos indivíduos mais aptos da geração anterior (os "melhores") 
    # e pelos novos filhos gerados.
    # a lista filhos é a lista de indivíduos gerados pelo cruzamento dos indivíduos mais aptos. 
    # Se houver mais filhos do que o espaço disponível na próxima geração (guardados em populaçao), 
    # apenas os primeiros filhos são selecionados.
    # tamanho_apos_cruzamento: é o número total de indivíduos desejado para a próxima geração após o cruzamento.
    # len(melhores): é o retorno do número de indivíduos na lista melhores.
    # Pega uma sublista de filhos começando do início da lista (filhos) até um índice determinado. 
    # O índice é calculado como :tamanho_apos_cruzamento menos o número do tamanho de melhores indivíduos (len(melhores)). 
    # Isso garante que o total de indivíduos na nova população não exceda tamanho_apos_cruzamento.
    populacao = melhores + filhos[:tamanho_apos_cruzamento - len(melhores)]

print("Melhores indivíduos encontrados que alcançaram a função objetivo:")
print(f"Quantidade de indivíduos encontrados: {len(individuos_que_alcancaram_objetivo)}")

if not individuos_que_alcancaram_objetivo:
    print("Não encontrado")
else:
    for individuo in individuos_que_alcancaram_objetivo:
        print(individuo)