lista =[0] *10

import random
for _ in range (10):
    lista.append(random.randint(0,15))

posi = []
for i in range (len(lista)):
    if lista[i] == 10:
        posi.append(i)

if posi:
    print("O elemento 10 aparece nos índices:", posi)
else:
    print("O elemento 10 não aparece na lista.")

print(lista)