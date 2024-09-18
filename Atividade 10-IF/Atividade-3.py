num = int(input("Digite a sua idade :"))

if  num < 12:
    print("Você é uma criança")

elif  12 <= num <= 18:
    print("Você é um adolescente")

elif 18 <= num <= 60:
    print("Você é um adulto")

elif num > 60:
    print("Você é um idoso")