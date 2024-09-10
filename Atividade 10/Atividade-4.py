sal = float(input("Digite seu salário: "))

if sal <= 1900:
    print("Você está isento.")

if 1901 <= sal <= 2800:
    conta = sal * 0.075
    print(f"Seu imposto de renda é: {conta}")

if sal == 2801 >= 3700:
    conta = sal * 0.15
    print(f"Seu imposto de renda é: {conta}")

if sal > 3700:
    conta = sal * 0.22
    print(f"Seu imposto de renda é: {conta}")