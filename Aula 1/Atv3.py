'''Paulo e Pedro fizeram uma longa viagem para a copa e tiveram que ajustar seus relógios por causa do fuso horário.
Assim, para melhor se organizarem para as próximas viagens, eles pediram que você fizesse um aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino com relação à origem, você informe a hora de chegada de cada voo no destino.
Entrada
A entrada contém 3 inteiros: S (0 ≤ S ≤ 23), T (1 ≤ T ≤ 12) e F (-5 ≤ F ≤ 5), separados por um espaço, indicando respectivamente a hora da saída, o tempo de viagem e o fuso horário do destino com relação à origem.'''

boolean = False
while boolean == False:
    exitHour, timeTravel, timezone, result = 0, 0, 0, 0
    exitHour = int(input("Qual o horário de saída? "))
    timeTravel = int(input("Qual o tempo da viagem? "))
    timezone = int(input("Qual o fuso horário do local? ")) 
    
    if exitHour >= 0 and exitHour <= 23:
        if timeTravel >= 1 and timeTravel <=12: 
            if timezone >= -5 and timezone <=5:
                result = exitHour + timeTravel + timezone
                boolean = True
                if result > 23:
                    result %= 24    
            else:
                print("Fuso horário inválido")
        else:
            print("Tempo de viagem inválido")
    else:
        print("Horário de saída inválido")

print("O indivíduo chegará às " + str(result) + " hora(s.)")