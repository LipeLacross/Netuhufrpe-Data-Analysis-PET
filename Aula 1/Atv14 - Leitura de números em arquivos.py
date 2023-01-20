'''Faça um programa que leia um número qualquer de notas em um arquivo. Após a leitura dos dados, faça o seguinte: 
Mostre a quantidade de notas que foram lidas. 
Exiba todas as notas na ordem em que foram informadas. 
Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
Calcule e mostre a soma das notas. 
Calcule e mostre a média das notas. 
Calcule e mostre a quantidade de notas acima da média calculada.'''

with open("Notas.txt", "r") as n:
    #print(n.read())#Ler o arquivo na ordem inicial
    #pegar linhas
    list = n.readlines()
    #mostrar lista
    for i in list:
        print(i)
    #inverter lista
    for i in range(len(list) - 1, 0, -1):
        print(list[i])
    print("\n")
    #Pegar apenas os valores
    values = []
    for i in list:
        values.append(i[7:8])
    print(values)
    #soma dos valores
    sum = 0
    for i in values:
        sum += int(i) 
    print(f"A soma deu {sum}")
    #média das notas
    average = sum/len(values)
    print(f"A média deu {average:.2f}")
    #notas acima da média
    highGrades = 0
    for i in values:
        if int(i) > average:
            highGrades += 1
    print(f"A quantidade de notas altas é {highGrades}")