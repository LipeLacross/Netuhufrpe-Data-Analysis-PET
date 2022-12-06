'''leia 5 valores inteiros. Conte valores digitados são pares e mostre essa informação.
Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''

valores = [1, 2, 3, 4, 7]
numerosPares = 0
for x in valores:
    if x % 2 == 0:
        numerosPares += 1
print(f"A quantidade de números pares é {numerosPares}")
        