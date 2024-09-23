velocidade_registrada = int(input("Digite a velocidade registrada do veículo: "))
limite_velocidade = float(input("Digite o limite de velocidade da via: "))

if velocidade_registrada > limite_velocidade:
    excesso_velocidade = velocidade_registrada - limite_velocidade
    if excesso_velocidade <= 10:
        multa = 50.00
    elif 11 <= excesso_velocidade <= 20:
        multa = 100.00
    else:
        multa = 200.00
    print(f"Você foi multado em R$ {multa:.2f}!")
else:
    print("Sem multa.")