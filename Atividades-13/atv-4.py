import time

# Pergunta ao usuário o número de segundos que ele deseja contar
segundos = int(input("Digite o número de segundos que você deseja contar: "))

# Inicializa o contador de segundos
contador = 0

# Conta de 0 até o número de segundos definido pelo usuário
while contador <= segundos:
    print(contador)  # Exibe o tempo passando em tempo real
    time.sleep(1)  # Faz uma pausa de 1 segundo entre as contagens
    contador += 1  # Incrementa o contador de segundos