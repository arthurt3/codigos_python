#1 forma de utilizar while - parecido com o FOR
contador = 1 #inicializando a variável 

while contador <= 5:
    print(contador)
    contador = contador + 1 # é o mesmo que contador +=1


print("="*48)

#2 forma de utilizar while  - loop condicional normal 

valor = 0 #inicializando a variável
while valor >=0:
        valor = int(input("Informe um valor qualquer (digite um valor negativo para terminar):"))

        print(f"Voce digitou {valor}")

print("="*48)

#3 forma de utilizar while - como se fosse faça..enquanto
while True:
            senha = input ("Informe a senha: ")
            if senha =="123":
                print ("Parabéns, Senha Correta")
                break #forma de encerrar o while
            else:
                print ("Senha incorreta,tente denovo")
