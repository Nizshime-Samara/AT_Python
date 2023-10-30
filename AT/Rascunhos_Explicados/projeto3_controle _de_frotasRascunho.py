'''
>>> Classes e seus atributos:
ItemEntrega: Representa um item a ser entregue.

identificador: Um identificador único para o item.
nome: Nome do item.
Local: Representa um local de entrega.

identificador: Identificador único para o local.
nome: Nome do local.
coordenadas: Uma tupla que representa a posição do local no plano (x, y).
itens: Lista de itens a serem entregues neste local.
Caminhao: Representa um caminhão.

placa: Identificação única do caminhão.
pontos_de_entrega: Lista de locais onde o caminhão deve entregar.

>>> Funções:
distancia(local1, local2): 
Calcula a distância euclidiana entre dois locais com base em suas coordenadas.

vizinho_mais_proximo(caminhao, locais_nao_visitados): 
Para um caminhão e um conjunto de locais não visitados, 
determina o próximo local mais próximo do último ponto de entrega do caminhão.

otimizar_rota_caminhao(caminhao, locais): 
Dado um caminhão e uma lista de locais, 
determina a rota otimizada usando o algoritmo do vizinho mais próximo.

>>> Variáveis globais:
caminhoes: Lista de todos os caminhões.
itens_de_entrega: Lista de todos os itens a serem entregues.
locais: Lista de todos os locais de entrega.

>>> Funcionalidades do menu:
inserir_ponto_de_entrega(): 
Solicita informações do usuário para criar um novo local e adiciona à lista global de locais.

inserir_item_de_entrega(): 
Solicita informações do usuário para criar um novo item e adiciona à lista global de itens.

associar_item_ponto(): 
Associa um item existente a um local de entrega existente, ou seja, diz que o item precisa ser entregue naquele local.

inserir_caminhao(): 
Adiciona um novo caminhão à lista global de caminhões.

associar_ponto_caminhao(): 
Usa a função otimizar_rota_caminhao para associar uma rota otimizada ao caminhão.

realizar_entregas(): 
Simula a entrega dos itens em cada ponto de entrega pelos caminhões. 
Ele mostra o percurso do caminhão e os itens entregues em cada local.

>>> Objetivo:
Quando um caminhão é associado a pontos de entrega,
o programa usa o algoritmo do vizinho mais próximo para otimizar a rota do caminhão, 
fazendo com que ele visite os locais na ordem que minimiza a distância total percorrida.

Abordagem implementada:
O Problema do Caixeiro Viajante (PCV) é um problema de otimização que busca determinar 
a menor rota que visita um conjunto de cidades e retorna à cidade original, visitando cada cidade exatamente uma vez.

***Foi escolhida  uma abordagem gulosa: 
Ela começa com uma cidade inicial e, em seguida, 
repetidamente visita a cidade mais próxima até que todas as cidades tenham sido visitadas.
A função 'find_next_closest_location' foi a responsável por implementar essa lógica, 
determinando o próximo ponto de entrega mais próximo com base na matriz de distâncias.

'''
import itertools
import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, outro_ponto):
        return math.sqrt((self.x - outro_ponto.x) ** 2 + (self.y - outro_ponto.y) ** 2)


class ItemEntrega:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

    def __str__(self):
        return self.nome


class Local:
    def __init__(self, identificador, nome, x, y):
        self.identificador = identificador
        self.nome = nome
        self.ponto = Ponto(x, y)
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def __str__(self):
        return self.nome


class Caminhao:
    def __init__(self, placa):
        self.placa = placa
        self.pontos_de_entrega = []

    def add_ponto_de_entrega(self, local):
        self.pontos_de_entrega.append(local)

    def __str__(self):
        return self.placa


caminhoes = []
itens_de_entrega = []
locais = []


def inserir_ponto_de_entrega():
    id_local = input("\nInsira um ID para o ponto de entrega: ")
    nome_local = input("Insira o nome do ponto de entrega: ")
    x, y = map(int, input("Insira as coordenadas do ponto (formato x y): ").split())
    local = Local(id_local, nome_local, x, y)
    locais.append(local)


def inserir_item_de_entrega():
    id_item = input("\nInsira um ID para o item de entrega: ")
    nome_item = input("Insira o nome do item de entrega: ")
    item = ItemEntrega(id_item, nome_item)
    itens_de_entrega.append(item)


def associar_item_ponto():
    id_item = input("\nInsira o ID do item de entrega: ")
    item = next((i for i in itens_de_entrega if i.identificador == id_item), None)
    id_local = input("Insira o ID do ponto de entrega: ")
    local = next((l for l in locais if l.identificador == id_local), None)
    if local:
        local.add_item(item)


def inserir_caminhao():
    placa = input("\nInsira a placa do caminhão: ")
    caminhao = Caminhao(placa)
    caminhoes.append(caminhao)


def associar_ponto_caminhao():
    id_local = input("\nInsira o ID do ponto de entrega: ")
    local = next((l for l in locais if l.identificador == id_local), None)
    placa = input("Insira a placa do caminhão: ")
    caminhao = next((c for c in caminhoes if c.placa == placa), None)
    if caminhao and local:
        caminhao.add_ponto_de_entrega(local)


def calcular_distancia_total(caminhao):
    distancia_total = 0
    ultimo_ponto = Ponto(0, 0)
    for local in caminhao.pontos_de_entrega:
        distancia_total += ultimo_ponto.distancia(local.ponto)
        ultimo_ponto = local.ponto
    distancia_total += ultimo_ponto.distancia(Ponto(0, 0))
    return distancia_total


def realizar_entregas():
    menor_distancia = float('inf')
    caminhao_menor_rota = None

    for caminhao in caminhoes:
        distancia_caminhao = calcular_distancia_total(caminhao)
        if distancia_caminhao < menor_distancia:
            menor_distancia = distancia_caminhao
            caminhao_menor_rota = caminhao

        print("\n--------------------------------------")
        print(f"Percurso do caminhão {caminhao.placa}:")
        for local in caminhao.pontos_de_entrega:
            print(f"Ponto de entrega {local.nome} foi visitado.")
            print("Itens entregues:")
            for item in local.itens:
                print(item.nome)
            print()

    print(f"\nO caminhão {caminhao_menor_rota.placa} fez a menor rota com uma distância total de {menor_distancia:.2f} unidades.")


def menu():
    while True:
        print("\n----------------- Menu -----------------")
        print("1 - Para inserir ponto de entrega.")
        print("2 - Para inserir item de entrega.")
        print("3 - Para inserir caminhão.")
        print("4 - Para associar item ao ponto de entrega.")
        print("5 - Para associar ponto de entrega ao caminhão.")
        print("6 - Realizar entregas.")
        print("0 - Sair.")
        opcao = input("\nSelecione uma opção: ")

        if opcao == "1":
            inserir_ponto_de_entrega()
        elif opcao == "2":
            inserir_item_de_entrega()
        elif opcao == "3":
            inserir_caminhao()
        elif opcao == "4":
            associar_item_ponto()
        elif opcao == "5":
            associar_ponto_caminhao()
        elif opcao == "6":
            realizar_entregas()
        elif opcao == "0":
            break

menu()