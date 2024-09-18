lista = [1 ,2 ,3]
lista1 =  [4 ,4 ,5] 

rsult = [0]
for i in range(len(lista)):
    rsult.append(lista[i] + lista1[i])

rsult.pop(0)

print("Resultado da soma das duas listas:", rsult)