meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
temperaturas = []
for i in range(12):
    temperaturas.append(
        float(input(f"Digite a temperatura de {meses[i]} em ºC: "))
    )

total = 0
for temp in temperaturas:
    total += temp
media = total/ len(temperaturas)


print(f"Média anual das temperaturas: {media:.2f}")

for i in range(len(temperaturas)): 
    temp = temperaturas[i] 
    if temp > media: 
        print(f"{meses[i]}: {temp:.2f}")