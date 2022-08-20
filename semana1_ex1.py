# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:07:38 2021


Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
Exemplos:

minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
3X1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
2X3


@author: Raphael Aguiar
"""

def dimensoes(matriz):
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    resultado = str(n_linha) + "X" + str(n_coluna)
    print(resultado)
    return


'''

minha_matriz = [[1], [2], [3]]
dimensaum = dimensoes(minha_matriz)
print(dimensaum)
# 3X1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
print(dimensoes(minha_matriz))
# 2X3

minha_matriz = [[1, 2], [3, 4]]
print(dimensoes(minha_matriz))
# 2X2

minha_matriz = [[1, 1], [1, 1]]
print(dimensoes(minha_matriz))
# 2X2

minha_matriz = [[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]]
print(dimensoes(minha_matriz))
# 4X4

minha_matriz = [[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1]]
print(dimensoes(minha_matriz))
# 3X4

minha_matriz = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(dimensoes(minha_matriz))
# 4X3

minha_matriz = [[1], [2]]
print(dimensoes(minha_matriz))
# 2X1

minha_matriz = [[1, 2]]
print(dimensoes(minha_matriz))
# 1X2

minha_matriz = [[1]]
print(dimensoes(minha_matriz))
# 1X1

'''