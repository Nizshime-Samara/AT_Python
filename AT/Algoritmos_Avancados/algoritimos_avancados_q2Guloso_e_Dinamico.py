
""" DESCRIÇÃO DO ALGORÍTIMO >> calcular_troco_guloso():
>>Objetivo central:
algoritmo é "guloso" porque faz a melhor escolha local (a moeda de maior valor possível) em cada etapa sem considerar 
as consequências a longo prazo dessa escolha. 
Ele faz isto ao ordenar os valores da lista de moedas da maior para a menor para tentar dar o troco usando o 
menor número de moedas possível, começando pelas moedas de maior valor e movendo-se para as de menor valor, 
e mantendo o registro das moedas usadas.

*** A eficiencia e complexidade do algorítimo vai depender de sua entrada para encontrar a soluçao global ótima.
"""
def calcular_troco_guloso(valor_total_de_troco_a_receber, lista_de_valores_diponiveis_de_moedas):
    quantidade_moedas = 0  
    moedas_selecionadas = [] 
    
    for moeda in reversed(lista_de_valores_diponiveis_de_moedas):  
        while valor_total_de_troco_a_receber >= moeda:
            valor_total_de_troco_a_receber -= moeda
            quantidade_moedas += 1
            moedas_selecionadas.append(moeda) 

    return (quantidade_moedas, moedas_selecionadas) if valor_total_de_troco_a_receber == 0 else (None, [])

lista_moedas = [1, 5, 10, 21, 25]
valor_total = 37

qtd_min_moedas_de_troco_a_devolver, moedas_selecionadas = calcular_troco_guloso(valor_total, lista_moedas)

print("------------------------------------------------------------------------------------")
print("Número total de moedas (Guloso):", qtd_min_moedas_de_troco_a_devolver, "moedas")
print("Moedas utilizadas (Guloso):", moedas_selecionadas)

""" DESCRIÇÃO DO ALGORÍTIMO >> calcular_troco_programacao_dinamica():

>> Objetivo central da função calcular_troco_programacao_dinamica:
Essencialmente, este algoritmo emprega a técnica de programação dinâmica para resolver o problema de forma eficiente,
construindo a solução a partir dos menores valores até o valor desejado.
"""
def calcular_troco_programacao_dinamica(valor_total_de_troco_a_receber, lista_de_valores_diponiveis_de_moedas):
    troco_min = [None] * (valor_total_de_troco_a_receber + 1) 
    moedas_usadas = [None] * (valor_total_de_troco_a_receber + 1)

    troco_min[0] = 0
    moedas_usadas[0] = []

    for i in range(1, valor_total_de_troco_a_receber + 1):
        for moeda in lista_de_valores_diponiveis_de_moedas:
                sub_resultado = troco_min[i - moeda]
                if sub_resultado is not None: 
                    if troco_min[i] is None or sub_resultado + 1 < troco_min[i]:
                        troco_min[i] = sub_resultado + 1 
                        moedas_usadas[i] = moedas_usadas[i - moeda] + [moeda]

    return troco_min[valor_total_de_troco_a_receber], moedas_usadas[valor_total_de_troco_a_receber]

lista_de_valores_de_moedas_disponiveis = [1, 5, 10, 21, 25]
valor_total_de_troco_a_receber = 37

qtd_min_moedas_de_troco_a_devolver, moedas_selecionadas = calcular_troco_programacao_dinamica(valor_total_de_troco_a_receber, lista_de_valores_de_moedas_disponiveis)

print("------------------------------------------------------------------------------------")
print("Número mínimo de moedas (Dinâmico):", qtd_min_moedas_de_troco_a_devolver, "moedas")
print("Moedas utilizadas (Dinâmico):", moedas_selecionadas)
print("------------------------------------------------------------------------------------")



