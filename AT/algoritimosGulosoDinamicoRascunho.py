def calcular_troco_guloso(valor_total_de_troco_a_receber, lista_de_valores_diponiveis_de_moedas):

    # inicializa a variável quantidade_moedas com 0. 
    # Esta variável manterá o registro do número total de moedas usadas para dar troco.
    quantidade_moedas = 0  
    # Esta linha inicializa uma lista vazia chamada moedas_selecionadas. 
    # Esta lista armazenará quais moedas específicas são usadas para dar troco.
    moedas_selecionadas = [] 

    #Loop for que que iterará sobre a lista de moedas disponíveis. 
    # No entanto, estamos usando reversed() para inverter a ordem das moedas, de forma que começaremos com a moeda de maior valor. 
    # O algoritmo guloso tenta usar os maiores valores primeiro.
    for moeda in reversed(lista_de_valores_diponiveis_de_moedas):  # Invertendo a lista para tentar as moedas de maior valor primeiro
        
        # Loop while que verifica se o valor_total_de_troco_a_receber é maior ou igual à moeda atual. 
        # Se for, podemos usar essa moeda como parte do troco.
        while valor_total_de_troco_a_receber >= moeda:

            # Aqui, estamos subtraindo o valor da moeda atual do valor_total_de_troco_a_receber. 
            # Isso nos ajuda a manter o registro de quanto ainda precisamos dar troco.
            valor_total_de_troco_a_receber -= moeda
            quantidade_moedas += 1
            moedas_selecionadas.append(moeda) 
    # Esta é uma expressão condicional. Se o valor_total_de_troco_a_receber é 0, 
    # significa que conseguimos dar o troco completo e retornamos a quantidade_moedas e moedas_selecionadas. 
    # Se não, retornamos None e uma lista vazia, indicando que não foi possível dar o troco com as moedas disponíveis.        
    return (quantidade_moedas, moedas_selecionadas) if valor_total_de_troco_a_receber == 0 else (None, [])

lista_moedas = [1, 5, 10, 21, 25]
valor_total = 37

qtd_min_moedas_de_troco_a_devolver, moedas_selecionadas = calcular_troco_guloso(valor_total, lista_moedas)

#################################################################################################################################
#################################################################################################################################

def calcular_troco_programacao_dinamica(valor_total_de_troco_a_receber, lista_de_valores_diponiveis_de_moedas):
    # Criada uma lista troco_min de tamanho valor_troco_total + 1 (38 posiçoes) onde todos os seus elementos são inicializados com o valor None. 
    # Esta é uma lista cujo objetivo é armazenar, para cada valor intermediário (de 0 até valor_total_de_troco_a_receber), 
    # o número mínimo de moedas necessárias para alcançar esse valor.
    troco_min = [None] * (valor_total_de_troco_a_receber + 1) 

    # Exceto a primeira posiçao troco_min[0], que é inicializada com valor 0. 
    # Ou seja, estamos definindo que o número mínimo de moedas(troco_min) para formar o valor 0 é 0, 
    # ou seja, não precisamos de nenhuma moeda para ter um valor de 0.
    troco_min[0] = 0 

    # Esse laço itera pelos valores intermediários de troco que queremos calcular. 
    # Para cada valor de i = 1, queremos saber o número mínimo de moedas necessárias para alcançar o de valor_total_de_troco_a_receber = 37 + 1.
    # Ou seja, para um valor_total_de_troco_a_receber igual a 37, ele vai considerar os valores de i até 38 
    # (38 por causa do uso da função range(), que age no intervalo de 1 até 36 (considerando que o valor_total_de_troco_a_receber seja igual a 37), 
    # excluindo o ponto fim 37, então para incluir o 37, precisa + 1).
    # Este loop externo vai iterar 37 vezes.
    for i in range(1, valor_total_de_troco_a_receber + 1):

        # Para cada valor intermediário i(representado por i no laço externo): 
        # este laço verifica cada moeda disponível na lista_de_valores_diponiveis_de_moedas 
        # para determinar se ela pode contribuir para formar o valor i .
        # para o valor intermediário atual i e a moeda atual moeda, estamos tentando verificar quantas moedas eram necessárias para formar o 
        # valor i - moeda. Esse valor anterior já foi calculado em uma iteração anterior e armazenado em troco_min.
        # Para cada iteração do loop externo, o loop interno será executado 5 vezes.
        # Ou seja, Número total de iterações = 37 (do loop externo) * 5 (do loop interno)
        # A complexidade de O(loop Externo * loopInterno) = 
        #  >>> O(valor_total_de_troco_a_receber * lista_de_valores_diponiveis_de_moedas)
        for moeda in lista_de_valores_diponiveis_de_moedas:

                # Calculando o Sub-resultado >> Verificação de Utilização da Moeda:
                # Verifica quantas moedas são necessárias para dar troco de um valor que é a diferença 
                # entre o valor intermediário atual "i" e o valor da moeda em consideração. 
                sub_resultado = troco_min[i - moeda]

                # Atualizando o Valor Mínimo de Moedas:
                # Aqui estamos checando se é possível usar a moeda atual moeda para formar o valor i. 
                # Se for porssível usar a moeda atual, e se a quantidade total de moedas usando essa moeda for menor do que a quantidade 
                # já registrada em troco_min[i], então atualizamos troco_min[i] com a nova contagem mínima.
                if sub_resultado is not None: 
                    if troco_min[i] is None or sub_resultado + 1 < troco_min[i]:
                        troco_min[i] = sub_resultado + 1 

    return troco_min[valor_total_de_troco_a_receber]

lista_de_valores_de_moedas_disponiveis = [1, 5, 10, 21, 25]
valor_total_de_troco_a_receber = 37

qtd_min_moedas_de_troco_a_devolver = calcular_troco_programacao_dinamica(valor_total_de_troco_a_receber, lista_de_valores_de_moedas_disponiveis)

print("Número mínimo de moedas (Dinâmico):", qtd_min_moedas_de_troco_a_devolver)