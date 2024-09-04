valor = float(input("informe seu salário:"))

if valor <=600:
    valor2 = (valor *1.3)
    print(f"o seu salário foi reajustado para {valor2:.2f}\n")
else:
    print(f"Infelizmente você não cumpre os requisitos\n")