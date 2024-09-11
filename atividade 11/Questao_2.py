qtd_negativos = 0
positivos = 0

for i in range(8):
    numero = int(input(f"Digite o {i+1} número: "))
    if numero < 0:
        qtd_negativos =  qtd_negativos + 1

    else:
        positivos = positivos + numero

print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {positivos}")