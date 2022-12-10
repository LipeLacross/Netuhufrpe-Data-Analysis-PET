'''Faça um programa que dado o salário bruto calcula o salário líquido. O salário líquido é calculado a partir do salário bruto, primeiro descontando 11% referente ao INSS, e do resultado, descontando-se 15% de imposto de renda (IR).
Exemplo
Salário Bruto = R$ 5000,00
Desconto do INSS = R$ 550,00 (11% de R$ 5000,00)
Desconto do IR = R$ 667,50 (15% de R$ 4450,00)
Salário L´ıquido = 5000 - (550 + 667,50) = 3782,50
'''

initialCash = float(input("Qual o valor sem descontos? "))
finalCash = 0

def inss(cash):
    inss = cash * 11 / 100
    cash -= inss
    return cash

def ir(cash):
    ir = cash * 15 / 100
    cash -= ir
    return cash

print("O salário líquido calculado: R$", str(ir(inss(initialCash))))