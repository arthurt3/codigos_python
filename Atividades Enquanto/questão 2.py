contador_impares = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 != 0:
        contador_impares += 1

print(f"Quantidade de números ímpares digitados: {contador_impares}")

