
# Aqui, estamos definindo uma função chamada calcular_troco_guloso 
# que aceita dois argumentos: valor e moedas.
def calcular_troco_guloso(valor, moedas):
    # Esta linha verifica se o valor que queremos dar de troco é igual a zero.
    #  Se for, significa que não precisamos dar troco,
    #  e a função retorna imediatamente 0 (nenhuma moeda necessária).
    if valor == 0:
        return 0

# Ordenamos a lista moedas em ordem decrescente. 
# Isso nos ajuda a começar a calcular o troco com as maiores moedas disponíveis primeiro.
    moedas = sorted(moedas, reverse=True)
    min_moedas = float('inf')

    for moeda in moedas:
        if valor >= moeda:
            sub_resultado = calcular_troco_guloso(valor - moeda, moedas) # recursividade aqui
            if sub_resultado + 1 < min_moedas:
                min_moedas = sub_resultado + 1

    return min_moedas

moedas = [1, 5, 10, 21, 25]
valor = 37
min_moedas = calcular_troco_guloso(valor, moedas)
print("Número mínimo de moedas (Guloso):", min_moedas)

def calcular_troco_programacao_dinamica(valor, moedas):
    # Criamos uma lista chamada 'troco_min' para acompanhar o número mínimo de moedas para cada valor de troco.
    # Inicializamos a lista com infinito para todos os valores, exceto para o valor zero, que é 0 moedas.
    troco_min = [float('inf')] * (valor + 1)
    troco_min[0] = 0

    # Começamos um loop de 1 até o valor de troco desejado.
    for i in range(1, valor + 1):
        # Agora, para cada valor de troco 'i', percorremos todas as moedas disponíveis.
        for moeda in moedas:
            # Verificamos se a moeda é menor ou igual ao valor de troco atual 'i'.
            if i >= moeda:
                # Calculamos o resultado mínimo anterior (sub_resultado) para o valor de troco 'i - moeda'.
                sub_resultado = troco_min[i - moeda]
                # Comparamos o sub_resultado + 1 (usando a moeda atual) com o valor mínimo encontrado até agora.
                # Se for menor, atualizamos o valor mínimo para o valor de troco 'i'.
                if sub_resultado + 1 < troco_min[i]:
                    troco_min[i] = sub_resultado + 1

    # No final do loop, 'troco_min[valor]' conterá o número mínimo de moedas necessário para dar o troco desejado.
    return troco_min[valor]

# Definimos as moedas disponíveis e o valor desejado para o troco.
moedas = [1, 5, 10, 21, 25]
valor = 37

# Chamamos a função 'calcular_troco_programacao_dinamica' com os valores e armazenamos o resultado em 'min_moedas'.
min_moedas = calcular_troco_programacao_dinamica(valor, moedas)

# Exibimos na tela o número mínimo de moedas necessário para dar o troco usando programação dinâmica.
print("Número mínimo de moedas (Programação Dinâmica):", min_moedas)


