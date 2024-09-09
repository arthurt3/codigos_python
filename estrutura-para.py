'''
Essa estrutura de repetição é o mais comum em qualquer outra linguagem de progamação

for (contador = 1; contador <=5; contdor++){



}
'''

#1 exemplo
for contador in range(1,6):
    print(contador)

print("-"*30)
#2 exemplo
for contador in range (1,11,2): # o 3 parametro irá aumentar o incremento dos valores que estão sendo exibidos
    print(contador)
print ("-"*30)
#3 exemplo - Números do maior para o menor
for contador in range(10,0,-1):
    print(contador,end=" ")# o comando end,informa como o paython irá mostrar o final de uma exibiçã,por padrão irá dar um enter(\n)  