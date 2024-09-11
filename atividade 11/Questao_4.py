num1 = int(input(f"Digite o 1º número: "))
num2 = int(input(f"Digite o 2º número: "))
num3 = int(input(f"Digite o 3º número: "))
num4 = int(input(f"Digite o 4º número: "))
num5 = int(input(f"Digite o 5º número: "))


m_numero = num1

numero = (num1, num2, num3, num4, num5)

for num in numero:
    if num > m_numero:
        m_numero = num

print(f"O maior número é {m_numero}")
