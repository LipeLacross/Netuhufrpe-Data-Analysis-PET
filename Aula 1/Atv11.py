'''Escreva uma função que recebe um array de caracteres e imprime o array de caracteres de trás pra frente.'''

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def reverseList(array):
    reverseListFinal = []
    for i in range(len(array) - 1, -1, -1):
        reverseListFinal.append(array[i]) 
    return reverseListFinal

print("A lista ao contrário fica: " + str(reverseList(list)))