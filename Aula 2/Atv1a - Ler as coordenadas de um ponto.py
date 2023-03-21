'''Faça um programa que leia as coordenadas de um ponto e em seguida mostre a qual quadrante esse ponto pertence

Em seguida, leia as coordenadas de mais cinco pontos e apresenta a distância entre ele e o primeiro ponto lido.'''
#Versão procedural

def readCoordinates(x1, x2, y1, y2):
    dif1 = (x2 - x1) ** 2
    dif2 = (y2 - y1) ** 2
    result = (dif1 + dif2) ** 1/2
    return result

num1 = int(input("Qual o x de A? "))
num2 = int(input("Qual o y de A? "))

num3 = int(input("Qual o x de B? "))
num4 = int(input("Qual o y de B? "))

num5 = int(input("Qual o x de C? "))
num6 = int(input("Qual o y de C? "))

num7 = int(input("Qual o x de D? "))
num8 = int(input("Qual o y de D? "))

print(readCoordinates(num1, num3, num2, num4))
print(readCoordinates(num1, num5, num2, num6))
print(readCoordinates(num1, num7, num2, num8))

