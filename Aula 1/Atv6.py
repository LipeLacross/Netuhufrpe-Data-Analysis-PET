'''Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.
Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.'''
import random

list = random.sample(range(1, 200), 100)#para criar uma lista de 100 números aleatórios entre 1 e 200
higherNumber = 0
index = 0

for i in range(len(list)):
    if list[i] > higherNumber:
        higherNumber = list[i]
        index = i
print(list) 
print("O maior número da lista é: " + str(higherNumber) + " e o índice desse valor é " + str(index))