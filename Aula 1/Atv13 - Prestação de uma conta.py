'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def paymentValue(value, days):
    totalValue = 0
    fees = 0
    if days == 0:
        return value
    else:
        totalValue = value + value * 0.03
        for i in range(days):
            totalValue = totalValue + totalValue * 0.001
        return totalValue

totalpayment = 0
accumulator = 0
while cashInput <= 0:
    cashInput = float(input('Digite o valor da prestação: '))
    daysInput = int(input('Digite o número de dias em atraso: '))
    totalpayment += paymentValue(cashInput, daysInput)
    accumulator += 1

print(f"Quantidade total de prestações: {accumulator}")
print(f"Valor total das prestações: {totalpayment}")

