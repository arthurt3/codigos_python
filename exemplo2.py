nome = input("Informe seu nome: ")
end = input("Informe seu endereço: ")
idade = input("Informe sua idade: ")

print(nome, end , idade)

print("Ola ", nome, " seu endereço é" , end, " sua idade é ", idade)

print("\nOla {} seu endereço é {} e sua idade é {}" .format(nome, end,idade))

print(f"\nBem Vind@ {nome}, você mora na {end} e tem {idade} anos")