'''Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Salve as listas PAR e IMPAR em um arquivo.'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def findPairsList(array):
    pairsList = []
    for i in range(0, len(array), 1):
        if  array[i] % 2 == 0:
            pairsList.append(array[i])
    return str(pairsList)

def findOddList(array):
    oddList = []
    for i in range(0, len(array), 1):
        if  array[i] % 2 != 0:
            oddList.append(array[i])
    return str(oddList)

with open("Pares.txt", "w") as p:
    p.writelines(findPairsList(list))
with open("Ímpares.txt", "w") as p:
    p.writelines(findOddList(list))    

print(findPairsList(list))
print(findOddList(list))
