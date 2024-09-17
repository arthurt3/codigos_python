soma_positivos = 0
soma_negativos = 0

for _ in range(10):
    valor = int(input("Digite um valor inteiro: "))
    if valor > 0:
        soma_positivos += valor
    elif valor < 0:
        soma_negativos += valor

print(f"Soma dos números positivos: {soma_positivos}")
print(f"Soma dos números negativos: {soma_negativos}")
