Crie um programa que receba o valor de uma compra e a quantidade de parcelas
desejadas (somente de 1 a 24). O programa deve calcular o valor da parcela,
aplicando juros de 1.5% ao mês se o número de parcelas for maior que 12. Exiba o
valor total a ser pago e o valor de cada parcela.


valor_compra = float(input("Digite o valor da compra: "))
qtd_parcelas = int(input("Digite a quantidade de parcelas de 1 à 24: "))

if qtd_parcelas <= 12:
    valorparcela = valor_compra / qtd_parcelas
    print(f"O valor total da compra é {valor_compra} e o valor de cada parcela é {qtd_parcelas}")