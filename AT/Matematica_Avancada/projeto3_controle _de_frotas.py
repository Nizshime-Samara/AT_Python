import math

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
        self.x = x
        self.y = y
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def __str__(self):
        return self.nome

class Caminhao:
    def __init__(self, placa):
        self.placa = placa
        self.pontos_de_entrega = []
        self.rota = []

    def __str__(self):
        return self.placa

caminhoes = []
itens_de_entrega = []
locais = []

def calcular_distancia(ponto1, ponto2):
    return math.sqrt((ponto1.x - ponto2.x)**2 + (ponto1.y - ponto2.y)**2)

def encontrar_rota_gulosa_para_caminhao(caminhao):
    locais_nao_visitados  = caminhao.pontos_de_entrega[:]
    current_location = locais_nao_visitados .pop(0)
    caminhao.rota.append(current_location)

    while locais_nao_visitados :
        next_location = min(locais_nao_visitados , key=lambda location: calcular_distancia(current_location, location))
        caminhao.rota.append(next_location)
        locais_nao_visitados .remove(next_location)
        current_location = next_location

def inserir_ponto_de_entrega():
    id_local = input("\nInsira um ID para o ponto de entrega: ")
    nome_local = input("Insira o nome do ponto de entrega: ")
    x, y = map(int, input("Insira as coordenadas do ponto (x y): ").split())
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
    caminhao.pontos_de_entrega.append(local)

def realizar_entregas():
    for caminhao in caminhoes:
        encontrar_rota_gulosa_para_caminhao(caminhao)
        print(f"\nCaminhão {caminhao.placa} percorreu os pontos na seguinte ordem:")
        for ponto in caminhao.rota:
            print(f" - {ponto.nome}")
            for item in ponto.itens:
                print(f"   -> Item entregue: {item.nome}")

def menu():
    while True:
        print("\n----------------- Menu -----------------")
        print("1 - Inserir ponto de entrega")
        print("2 - Inserir item de entrega")
        print("3 - Inserir caminhão")
        print("4 - Associar item ao ponto de entrega")
        print("5 - Associar ponto de entrega ao caminhão")
        print("6 - Realizar entregas")
        print("0 - Sair")
        opcao = input("Selecione uma opção: ")
        
        if opcao == "1": inserir_ponto_de_entrega()
        elif opcao == "2": inserir_item_de_entrega()
        elif opcao == "3": inserir_caminhao()
        elif opcao == "4": associar_item_ponto()
        elif opcao == "5": associar_ponto_caminhao()
        elif opcao == "6": realizar_entregas()
        elif opcao == "0": break

menu()