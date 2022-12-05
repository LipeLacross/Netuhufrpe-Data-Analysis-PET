'''Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.
Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.
Saída
A saída contém um valor correspondente à média de idade dos indivíduos.
'''
ages = []
newAge = 1
iterator = 0
totalSum = 0

while newAge >= 0:
    newAge = int(input("Insira uma idade: "))
    ages.append(newAge)
ages.pop()

for i in range(0 , len(ages), 1):
    iterator += 1
    totalSum += ages[i]

average = totalSum / iterator
print("A média total é " + str(average))
