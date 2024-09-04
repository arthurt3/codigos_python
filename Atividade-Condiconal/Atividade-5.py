km = float(input("Quantos kms irão ser percorridos?"))
car =int(input("Qual o modelo do carro 1, 2 ou 3?"))

if car ==1:
    cdc= (km/8)

    print(f"O consumo estimado vai ser de {cdc:.2f}")
elif car == 2: 
    cdc= (km/9)
    print(f"O consumo estimado vai ser de {cdc:.2f}")
elif car == 3: 
    cdc= (km/12)
    print(f"O consumo estimado vai ser de {cdc:.2f}")