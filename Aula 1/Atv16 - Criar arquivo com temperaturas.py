'''Faça um programa que leia a temperatura média de cada mês do ano em um arquivo e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

months = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]
listTemperatures = []
for i in range(0, len(months), 1):
    listTemperatures.append(
        float(input(f"Digite a temperatura de {months[i]} em ºC: "))
    )

#listTemperatures.extend([janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro])#adicionar variáveis de uma vez a uma lista
print("Lista de temperaturas: " + str(listTemperatures))

temperaturesSum = 0
iterator = 0
for i in range(1, len(listTemperatures), 1):
    temperaturesSum += listTemperatures[i]
    iterator = iterator + 1
averageSum = temperaturesSum / iterator

print("Média da temperatura anual: " + str(round(averageSum, 2)))

with open("Temperatura.txt", "w") as t:
    for i  in range(0, len(months), 1):
        t.write(f"Mês de {months[i]} - {listTemperatures[i]}ºC\n")
    t.write(f"A média das temperaturas resultou em {averageSum:.1f}ºC")