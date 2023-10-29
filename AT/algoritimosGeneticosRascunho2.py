import random

def calcular_aptidao(individuo):
    return sum(individuo)

def merge_sort(populacao):
    if len(populacao) <= 1:
        return populacao

    meio = len(populacao) // 2
    esquerda = merge_sort(populacao[:meio])
    direita = merge_sort(populacao[meio:])

    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    result = []
    esq_idx, dir_idx = 0, 0

    while esq_idx < len(esquerda) and dir_idx < len(direita):
        if calcular_aptidao(esquerda[esq_idx]) > calcular_aptidao(direita[dir_idx]):
            result.append(esquerda[esq_idx])
            esq_idx += 1
        else:
            result.append(direita[dir_idx])
            dir_idx += 1

    result.extend(esquerda[esq_idx:])
    result.extend(direita[dir_idx:])
    
    return result

def selecionar_melhores(populacao, tamanho_selecao):
    return populacao[:tamanho_selecao]

def realizar_crossover(individuo1, individuo2):
    ponto_crossover = random.randint(1, 5)
    filho1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    filho2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]
    return filho1, filho2

def realizar_mutacao(individuo, taxa_mutacao):
    for _ in range(3):
        if random.random() < taxa_mutacao:
            gene = random.randint(0, 5)
            individuo[gene] = 1 - individuo[gene]

tamanho_populacao = 4 
tamanho_apos_cruzamento = 8
tamanho_selecao = 4
geracoes_max = 16
taxa_mutacao = 0.005
funcao_objetivo = 6

populacao = []

for _ in range(tamanho_populacao):
    print(f"Digite os 6 genes (0 ou 1) para o indivíduo {_ + 1} sem espaços:")
    entrada = input("Genes: ")
    genes = [int(gene) for gene in entrada]
    if len(genes) != 6:
        print("Você deve fornecer exatamente 6 genes. Tente novamente.")
        continue
    populacao.append(genes)

individuos_alcancaram_objetivo = []

for geracao in range(geracoes_max):
    populacao = merge_sort(populacao)

    if calcular_aptidao(populacao[0]) == funcao_objetivo:
        individuos_alcancaram_objetivo.append(populacao[0].copy())

    melhores = selecionar_melhores(populacao, tamanho_selecao)

    filhos = []
    while len(filhos) < tamanho_apos_cruzamento:
        pai1, pai2 = random.sample(melhores, 2)
        filho1, filho2 = realizar_crossover(pai1, pai2)
        realizar_mutacao(filho1, taxa_mutacao)
        realizar_mutacao(filho2, taxa_mutacao)
        filhos.append(filho1)
        if len(filhos) < tamanho_apos_cruzamento:
            filhos.append(filho2)

    populacao = melhores + filhos[:tamanho_apos_cruzamento - len(melhores)]

print("Melhores indivíduos encontrados que alcançaram a função objetivo:")
print(f"Quantidade de indivíduos encontrados: {len(individuos_alcancaram_objetivo)}")

if not individuos_alcancaram_objetivo:
    print("Não encontrado")
else:
    for individuo in individuos_alcancaram_objetivo:
        print(individuo)