'''Faça um programa que leia as coordenadas de um ponto e em seguida mostre a qual quadrante esse ponto pertence

Em seguida, leia as coordenadas de mais cinco pontos e apresenta a distância entre ele e o primeiro ponto lido.'''
#Versão com classe

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def readCoordinates(self, anotherPoint):
        dif1 = (anotherPoint.x - self.x) ** 2
        dif2 = (anotherPoint.y - self.y) ** 2
        result = (dif1 + dif2) ** 1/2
        return result
    
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return "primeiro quadrante"
        elif self.x < 0 and self.y > 0:
            return "segundo quadrante"
        elif self.x < 0 and self.y < 0:
            return "terceiro quadrante"
        elif self.x > 0 and self.y < 0:
            return "quarto quadrante"
        else:
            return "quadrante nulo"

p1 = Coordinates(1, 2)
px2 = int(input("Qual o x de p2? "))
py2 = int(input("Qual o y de p2? "))
p2 = (px2, py2)

class circumference():
    def __init__(self, ponto, raio):
        self.center = ponto
        self.radius = raio

    def pertence(self, p):
        if self.center.distancia(p) <= self.radius:
            return True
        else:
            return False

dist = p.distancia(p2)
print(dist)
print(p.quadrante())
print(p2.quadrante())

c = Circuferencia(p, 1)
respo = c.pertence(p2)
print(respo)
