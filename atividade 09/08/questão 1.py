soma = 0
contagem = 0

for numero in range(50,70):
    if numero % 2 == 0:
        soma += numero
        contagem += 1

média = soma / contagem

print(f"Soma dos valores pares: {soma}")
print(f"Média aritmética dos valores pares: {média}")
print(f"Total de números lidos: {contagem}")