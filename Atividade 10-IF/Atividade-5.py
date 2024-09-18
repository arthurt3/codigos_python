qtdh = float(input("Digite sua quantidade de horas trabalhadas: "))
valh = float(input("Digite seu valor por hora: "))

aum = 50/100

if valh >= 40:
    conta = valh * aum
    print("Você receberá um bônus de 50% sobre as horas extras.")
else:
    print("Você não tem direito ao aumento.")