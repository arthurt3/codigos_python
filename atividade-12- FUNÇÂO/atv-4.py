# Crie o dicionário com 8 tipos de itens e suas quantidades iniciais
itens_vendidos = {
    "camisas": 0,
    "sapatos": 0,
    "calças": 0,
    "blusas": 0,
    "vestidos": 0,
    "ternos": 0,
    "shorts": 0,
    "meias": 0
}

# Função para atualizar a quantidade de um item específico
def atualiza_itens(item, quantidade):
    if item in itens_vendidos:
        itens_vendidos[item] += quantidade
        print("Quantidade atualizada com sucesso!")
        print("Itens vendidos atualizados:")
        print(itens_vendidos)
    else:
        print("Item não encontrado no dicionário.")

atualiza_itens("camisas", 5)  # Atualize a quantidade de "camisas" em 5
atualiza_itens("sapatos", 2)  # Atualize a quantidade de “sapatos” por 2