# Criando o dicionário de preços de produtos
precos_produtos = {}

# Solicitando o nome e o preço de 4 produtos ao usuário
for i in range(4):
    produto = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {produto}: R$"))
    precos_produtos[produto] = preco

# Solicitando o nome do produto ao usuário
produto = input("Digite o nome do produto que você deseja consultar: ")

# Verificando se o produto está no dicionário
if produto in precos_produtos:
    # Exibindo o preço do produto
    print(f"O preço do {produto} é R${precos_produtos[produto]:.2f}")
else:
    # Exibindo uma mensagem informando que o produto não foi encontrado
    print(f"O produto {produto} não foi encontrado.")