'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
Entrada
Quatro números inteiros representando a hora de início e fim do jogo.
Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

initialHour = int(input("Digite a hora inicial:"))
#11:00
finalHour = int(input("Digite a hora final: "))
#01:00
initialMinute = int(input("Digite o minuto inicial: "))
#XX:40
finalMinute = int(input("Digite o minuto final: "))
#XX:20
resultHour = finalHour - initialHour
resultMinute = finalMinute - initialMinute
if initialHour >= finalHour:
    resultHour = 24 - initialHour + finalHour
if initialMinute > finalMinute:
    resultMinute = 60 - initialMinute + finalMinute

print("O jogo durou " + str(resultHour) + " hora(s) e " + str(resultMinute) + " minuto(s).")
