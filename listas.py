animais = ['cachorro','gato', 'ovelha']
print(type(animais))#exibindo o tipo da variável

print(animais)

print('-'*50)
#estamos exibindo todos os items da lista animais 
for elementos in animais:
    print(elementos)

#1ª etapa: Atualização de dados
print('-'*50)
animais[0] = 'Coelho'
print(animais)

#2ª etapa: Inserir itens na lista
print('-'*50)
#forma 1 - usando append
animais.append("Cavalo")#irá inserir um novo item no final da lista
print(animais)

#Forma 2 - usando insert
print('-'*50)
animais.insert(2,"Pássaro")# O insert precisa de 2 valor, o 1 será o índice da lista que desejo inserir o valor. O 2ª é o conteúdp que quero inserir na lista
print(animais)

#3ª etapa: Excluir itens na lista
print('-'*50)
#forma 1 - usando pop()
animais.pop()# Irá sempre excluir o ultimo item
print(animais)

#forma  2 - usando pop() com índice
animais.pop(1)#irá excluir o item que está no índice 1
print(animais)

#forma 3 usando remvoce()
animais.remove("gato")#irá excluir o item que está na lista
print(animais)