# Inicialize um dicionário vazio
lista_telefonica = {}

# Peça ao usuário para inserir o número de pessoas
num_pessoas = int(input("Insira o número de pessoas: "))

# Loop por cada pessoa e peça seu nome e número de telefone
for i in range(num_pessoas):
    nome = input(f"Insira o nome da pessoa {i+1}: ")
    numero_telefone = input(f"Insira o número de telefone de {nome}: ")
    lista_telefonica[nome] = numero_telefone

# Imprima o dicionário da lista de telefones
print("Lista de Telefones:")
for nome, numero_telefone in lista_telefonica.items():
    print(f"{nome}: {numero_telefone}")