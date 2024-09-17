valores = []
for i in range (7): 
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)

#calculando a quntidade de números ímpares na lista
imp = 0
for numero in valores:
    if numero % 2 != 0:
        imp += 1

#Mostrando a quantidade de números ímpares na lista
print(f"Existem {imp} números ímpares")