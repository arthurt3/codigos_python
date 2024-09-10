somar_pesos = 0
somar_idades = 0


for contador in range(5):
    peso = float(input("Informe seu peso(kg): "))
    idade = int(input("Informe sua idade: "))

    somar_pesos = somar_pesos + peso
    somar_idades = somar_idades + idade

print (f"A média de peso do time é {somar_pesos/5}")
print (f"A média de idade do time é {somar_idades/5}")