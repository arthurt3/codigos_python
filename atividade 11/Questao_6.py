num = int(input("Digite um número: "))

smd = 0

for i in range (1, num):
    if num % i == 0:
        smd = smd + i

if smd == num:
    print(f"{num} é um número perfeito")
else:
    print(f"{num} não é um número perfeito")

