'''Dada uma lista, leia 100 valores inteiros, e inclua-os na lista. Apresente então o maior e menor valores lidos e a posição deles.
Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.
Saída
Apresenta os valores lidos e a posição de entrada.'''
import random

list = random.sample(range(1, 200), 100)

higherNumber = 0
lowerNumber = 9999999999999999999999999999999999999999999999999999999999
higherNumberIndex = 0
lowerNumberIndex = 0
for i in range(0, len(list), 1):
    if list[i] > higherNumber:
        higherNumber = list[i]
        higherNumberIndex = i
    if list[i] < lowerNumber:
        lowerNumber = list[i]
        lowerNumberIndex = i

print(list)
print("O maior número da lista é: " + str(higherNumber) + " e o índice desse valor é " + str(higherNumberIndex))
print("O menor número da lista é: " + str(lowerNumber) + " e o índice desse valor é " + str(lowerNumberIndex))