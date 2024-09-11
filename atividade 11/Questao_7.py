num = int(input("Digite um número inteiro positivo: "))
num2 = int(input("Digite um segundo número inteiro positivo: "))

nmt = num2 + 1
cont = 0

for i in range(num, nmt):
    if i % 7 == 0 and i % 11 == 0:
        cont += 1


print(f"O total de números entre {num} e {num2} que são múltiplos de 7 e 11 simultaneamente é: {cont}")
