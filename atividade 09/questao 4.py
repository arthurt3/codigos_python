val_inicial = int(input("Informe um valor inicial :"))
val_final = int(input("Informe um valor final: "))

soma = 0 #inicalizando a variável
for contador in range(val_inicial, val_final+1):
    soma= soma + contador

print (f"A soma do intervalo da de {val_inicial} até {val_final} é {soma}")