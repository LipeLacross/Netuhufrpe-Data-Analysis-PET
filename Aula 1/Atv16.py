'''Faça um programa que leia a temperatura média de cada mês do ano em um arquivo e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

listTemperatures = []

january   = int(input("Qual a temperatura média em janeiro? "))
february  = int(input("Qual a temperatura média em fevereiro? "))
march     = int(input("Qual a temperatura média em março? "))
april     = int(input("Qual a temperatura média em abril? "))
may       = int(input("Qual a temperatura média em maio? "))
june      = int(input("Qual a temperatura média em junho? "))
july      = int(input("Qual a temperatura média em julho? "))
august    = int(input("Qual a temperatura média em agosto? "))
september = int(input("Qual a temperatura média em setembro? "))
october   = int(input("Qual a temperatura média em outubro? "))
november  = int(input("Qual a temperatura média em novembro? "))
december  = int(input("Qual a temperatura média em dezembro? "))
listTemperatures.extend([january, february, march, april, may, june, july, august, september, october, november, december])
print("Lista de temperaturas: " + str(listTemperatures))

temperaturesSum = 0
iterator = 0
for i in range(1, len(listTemperatures), 1):
    temperaturesSum += listTemperatures[i]
    iterator = iterator + 1
averageSum = temperaturesSum / iterator
print("Média da temperatura anual: " + str(round(averageSum, 2)))
