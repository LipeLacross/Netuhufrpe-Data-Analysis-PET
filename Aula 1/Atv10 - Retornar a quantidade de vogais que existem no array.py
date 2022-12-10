'''Escreva uma função que recebe um array de caracteres e retorna a quantidade de vogais que existem no array.'''
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "e", "i", "o", "u"]

def findVowelsList(array):
    vowelsList = []
    score = 0
    for i in range(0, len(array), 1):  
        if array[i]  == "a" or array[i] == "e" or array[i] == "i" or array[i] == "o" or array[i] == "u":
            score += 1 
    return score

print("A quantidade de vogais é " + str(findVowelsList(list)))