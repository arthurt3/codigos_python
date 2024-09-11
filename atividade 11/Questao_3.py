menor = 0
igual = 0
media = 33.5

for i in range(7):
    temp = int(input(f"Digite a {i+1} temperatura: "))
    if temp < media:
        menor =  menor + 1

    elif  temp >= media:

        igual = igual + 1

print(f"Quantidade de temperaturas menor que a média: {menor}")
print(f"Quantidade de temperaturas maior ou igual que a média: {igual}")