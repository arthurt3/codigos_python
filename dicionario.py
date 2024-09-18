pessoa = ["Maria","48","rua 10"]
print(pessoa)

#Iniciando com dicionário
dados_pessoais = {
    'nome':'João',
    "idade":23,
    "endereco": "avenida 4"
}

print(dados_pessoais)

#Exibindo as chaves utilizando o comando keys()

print(dados_pessoais.keys())

#Exibindo as chaves utilizando o comando values()

print(dados_pessoais.values())

#Exibindo as chaves utilizando o comando items()

print(dados_pessoais.items())

#Exibindo o dicionario detalhado

for chave, valor in dados_pessoais.items():
    print(f"{chave} = {valor}")

#Realizando operações  com dicionários
#Adcionando dados ao dicionário
#Forma  1
dados_pessoais["Pesos"] = 68
print(dados_pessoais)

#Forma 2 - usando o comando update
dados_pessoais.update({"Profissão: Engenheiro"})
print(dados_pessoais)

#remover dados do dicionário
#Forma 1 - usando o comando pop()
dados_pessoais.pop("idade")# preciso passar a chave para podeer excluir o registro
print(dados_pessoais)

#Forma 2 - usando del()
del(dados_pessoais["endereco"])
print(dados_pessoais)