print("Se seu sexo for feminino digite 1, se for masculino digite 2")
sexo =int(input("Opção 1 ou 2?"))
alt = float(input("Qual sua altura em metros?"))

if sexo == 1:
    pf= ((62.1 * alt)-44.7)
    print(f"Seu peso ideal é {pf:.2f}")
elif sexo == 2: 
    pm = ((72.7 * alt) - 58)
    print(f"Seu peso ideal é {pm:.2f}")
