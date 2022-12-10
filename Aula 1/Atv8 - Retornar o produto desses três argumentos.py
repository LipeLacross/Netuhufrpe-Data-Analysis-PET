'''Fazer uma função que recebe três argumentos, e que retorne o produto desses três argumentos.
Fazer uma função que receba como parâmetro um número inteiro e retorne o fatorial desse número (não usar recursividade).'''

def produto(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado
print(produto(2, 3, 5))

def fatorial(num1):
    iterator = num1 #iterador = 3 
    fat = 0
    while iterator > 1: #3 > 1? | 2 > 1?
        iterator -= 1 #iterador = 2 | iterador = 1
        fat = num1 * iterator  # 3 * 2 = 6 | 6 * 1 = 3
        num1 = fat
    return fat
print(fatorial(3))