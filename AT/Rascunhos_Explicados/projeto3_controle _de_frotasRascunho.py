class ItemEntrega:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

    def __str__(self):
        return self.nome

class Local:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def remove_item(self, item):
        self.itens.remove(item)

    def __str__(self):
        return self.nome

class Caminhao:
    def __init__(self, placa):
        self.placa = placa
        self.pontos_de_entrega = []
        self.itens_na_cacamba = []

    def add_ponto_de_entrega(self, local):
        self.pontos_de_entrega.append(local)

    def remove_ponto_de_entrega(self, local):
        self.pontos_de_entrega.remove(local)

    def add_item_na_cacamba(self, item):
        if len(self.itens_na_cacamba) < 20:
            self.itens_na_cacamba.append(item)
            return True
        return False

    def remove_item_na_cacamba(self):
        if self.itens_na_cacamba:
            return self.itens_na_cacamba.pop()
        return None

    def topo_da_cacamba(self):
        if self.itens_na_cacamba:
            return self.itens_na_cacamba[-1]
        return None

    def __str__(self):
        return self.placa
    
caminhoes = []
itens_de_entrega = []
locais = []

def inserir_ponto_de_entrega():
    id_local = input("\nInsira um ID para o ponto de entrega: ")
    # Verifica se o ID já existe
    if any(l for l in locais if l.identificador == id_local):
        print("Erro: ID do ponto de entrega já existe.")
        return
    nome_local = input("\nInsira o nome do ponto de entrega: ")
    local = Local(id_local, nome_local)
    locais.append(local)

def inserir_item_de_entrega():
    id_item = input("\nInsira um ID para o item de entrega: ")
    # Verifica se o ID já existe
    if any(i for i in itens_de_entrega if i.identificador == id_item):
        print("Erro: ID do item já existe.")
        return
    nome_item = input("\nInsira o nome do item de entrega: ")
    item = ItemEntrega(id_item, nome_item)
    itens_de_entrega.append(item)

def associar_item_ponto():
    id_item = input("\nInsira o ID do item de entrega: ")
    item = next((i for i in itens_de_entrega if i.identificador == id_item), None)
    if not item:
        print("Erro: ID do item não encontrado.")
        return
    id_local = input("\nInsira o ID  do ponto de entrega: ")
    local = next((l for l in locais if l.identificador == id_local), None)
    if not local:
        print("Erro: ID do ponto de entrega não encontrado.")
        return
    local.add_item(item)

def inserir_caminhao():
    placa = input("\nInsira a placa do caminhão: ")
    caminhao = Caminhao(placa)
    caminhoes.append(caminhao)    

def associar_ponto_caminhao():
    id_local = input("\nInsira o ID do ponto de entrega: ")
    local = next((l for l in locais if l.identificador == id_local), None)
    if not local:
        print("Erro: ID do ponto de entrega não encontrado.")
        return
    placa = input("\nInsira a placa do caminhão: ")
    caminhao = next((c for c in caminhoes if c.placa == placa), None)
    if not caminhao:
        print("Erro: Placa do caminhão não encontrada.")
        return
    caminhao.add_ponto_de_entrega(local)

def realizar_entregas():
    for caminhao in caminhoes:
        print("--------------------------------------")
        print(f"Percurso do caminhão {caminhao.placa}:")
        total_itens = 0
        for local in caminhao.pontos_de_entrega:
            print(f"Ponto de entrega {local.nome} foi visitado.")
            print(f"Foram entregues os itens:")
            for item in local.itens:
                print(item.nome)
                total_itens += 1   
            print()
        print(f">>>Total de pontos de entrega: {len(caminhao.pontos_de_entrega)}")
        print(f"\n>>>Total de itens entregues: {total_itens}")

def menu():
    while True:
        print("----------------- Menu -----------------")
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
