import random
numeros = [random.randint(1,6) for _ in range (10)]

cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0

for  num in numeros:
    if num == 1:
        cont_1 += 1
    elif num == 2: 
        cont_2 += 1
    elif num == 3:
        cont_3 += 1
    elif num ==  4:
        cont_4 += 1
    elif num == 5:
        cont_5 += 1
    elif num == 6:
        cont_6 += 1

print(f"Números sorteados {numeros} ")
print(f"A frequência dos números")
print(f"1:{cont_1}")
print(f"2:{cont_2}")
print(f"3:{cont_3}")
print(f"4:{cont_4}")
print(f"5:{cont_5}")
print(f"6:{cont_6}")