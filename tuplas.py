#trabalhando com tuplas

objetos = ('Lápis',  'Caneta', 'Borracha')

print(type(objetos)) # a funçao type irá exibir o tipo de variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)

print(objetos[1])

#exibindo todos os dados da tupla
for item in range(0,3):
    print(objetos[item])

#exibindo todos  os dados da tupla de forma mais simples
print('-'*50)

for item in objetos:
    print(item)

#tentando mudar o conteúdo da tupla
print('-'*50)

objetos[0] = 'Caderno' #Irá ocorrer um erro pois os valores de uma tupla são imutáveis
print(objetos)