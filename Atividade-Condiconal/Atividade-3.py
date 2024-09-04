valor = float(input("informe seu salário:"))

finan = float(input("informe o financimento desejado:"))

total = valor *5

if finan <= total:
    print("Seu financiamento foi concedido\n") 
else:
    print("Seu Financiamento foi negado\n") 

print("\n")
print("Obrigado por nos consultar")