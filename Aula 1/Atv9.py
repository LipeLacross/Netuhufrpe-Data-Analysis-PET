'''Escreva uma função que recebe um parâmetro: um array de inteiros e imprime todos os números pares desse array'''

list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def findPairsList(array):
    pairsList = []
    for i in range(0, len(array), 1):
        if  array[i] % 2 == 0:
            pairsList.append(array[i])
    return pairsList

print("A lista de números pares é " + str(findPairsList(list)))