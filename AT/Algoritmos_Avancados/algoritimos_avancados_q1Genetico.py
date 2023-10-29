import random # usado para gerar números aleatórios.

# Esta função calcula a aptidão de um indivíduo, que é a soma de seus genes.
#  Quanto mais próximo a soma for de 6, melhor é a aptidão.
def calcular_aptidao(individuo):
    return sum(individuo)

# Esta função classifica a população com base na aptidão de seus 
# indivíduos, em ordem decrescente.
def ordenar_populacao(populacao):
    return sorted(populacao, key=calcular_aptidao, reverse=True)

# Essa função seleciona os melhores indivíduos da população com base na classificação da aptidão.
#  O número de indivíduos  selecionados é determinado pelo parâmetro tamanho_selecao.
def selecionar_melhores(populacao, tamanho_selecao):
    return populacao[:tamanho_selecao]

# O crossover é uma operação genética que mistura genes de dois indivíduos
#  para criar dois filhos. Neste código, o ponto de crossover é escolhido 
# aleatoriamente entre 1 e 5 (índices dos genes). 
# O código realiza o crossover criando dois filhos, 
# onde o filho 1 pega os primeiros genes do pai 1 e os
#  últimos genes do pai 2, e o filho 2 pega os primeiros genes do pai 2 
# e os últimos genes do pai 1.
def realizar_crossover(individuo1, individuo2):
    ponto_crossover = random.randint(1, 5)
    filho1 = individuo1[:ponto_crossover] + individuo2[ponto_crossover:]
    filho2 = individuo2[:ponto_crossover] + individuo1[ponto_crossover:]
    return filho1, filho2

# A mutação é uma operação genética que pode alterar aleatoriamente um gene do indivíduo. 
# Neste código, a mutação ocorre com uma probabilidade determinada 
# pela taxa de mutação (taxa_mutacao). 
# Se a probabilidade de mutação for atendida, 
# um gene é escolhido aleatoriamente e trocado (de 0 para 1 ou de 1 para 0).
def realizar_mutacao(individuo, taxa_mutacao):
    for _ in range(3):
        if random.random() < taxa_mutacao:
            gene = random.randint(0, 5)
            individuo[gene] = 1 - individuo[gene]

# As variáveis 
# tamanho_populacao:  O tamanho da população inicial.
#  tamanho_apos_cruzamento: O tamanho da população após o cruzamento.
# tamanho_selecao: O número de indivíduos selecionados como os melhores em cada geração.
# geracoes_max: O número máximo de gerações que o algoritmo executará.
# taxa_mutacao: A probabilidade percentual de ocorrer uma mutação em um gene durante o processo.
# funcao_objetivo:  O valor que se deseja alcançar como objetivo (6 neste caso). 
tamanho_populacao = 5 
tamanho_apos_cruzamento = 10
tamanho_selecao = 5
geracoes_max = 20
taxa_mutacao = 0.005
funcao_objetivo = 6

# Solicita ao usuário uma lista de indivíduos com os 6 genes 
populacao = []
# Em seguida, o código entra em um loop para as gerações. 
# Dentro desse loop, ele ordena a população atual com base na aptidão, 
# verifica se algum indivíduo alcançou a função objetivo (soma igual a 6),
#  seleciona os melhores indivíduos, realiza o crossover e a 
# mutação nos filhos gerados.
for _ in range(tamanho_populacao):
    print(f"Digite os 6 genes (0 ou 1) para o indivíduo {_ + 1} sem espaços:")
    entrada = input("Genes: ")
    genes = [int(gene) for gene in entrada]
    if len(genes) != 6:
        print("Você deve fornecer exatamente 6 genes. Tente novamente.")
        continue
    populacao.append(genes)

individuos_alcancaram_objetivo = []

# O loop de gerações continua até atingir o 
# número máximo de gerações especificado (geracoes_max).
for geracao in range(geracoes_max):
    populacao = ordenar_populacao(populacao)

    # Verifica se a função objetivo foi alcançada 
    # (soma dos genes que deve ser igual a 6)
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

# No final, o código imprime os melhores indivíduos 
# que alcançaram a função objetivo.
# Caso nao encontre, imprime a mensagem "Não encontrado"
print("Melhores indivíduos encontrados que alcançaram a função objetivo:")
if not individuos_alcancaram_objetivo:
    print("Não encontrado")
else:
    for individuo in individuos_alcancaram_objetivo:
        print(individuo)

