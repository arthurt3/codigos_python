def add_temperatura():
    # Inicializa um dicionário vazio para armazenar as temperaturas
    temperaturas = {}

    # Solicita 5 temperaturas e armazena no dicionário
    for i in range(5):
        temperatura = float(input(f"Digite a temperatura {i+1} (em graus Celsius): "))
        temperaturas[f"Temperatura {i+1}"] = temperatura

    # Exibe o dicionário com as temperaturas
    print("\nDicionário com as temperaturas:")
    for chave, valor in temperaturas.items():
        print(f"{chave}: {valor}°C")

# Chama a função
add_temperatura()   