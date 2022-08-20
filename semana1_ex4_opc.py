

def sao_multiplicaveis(m1, m2):
    ncolm1 = len(m1[0])
    nlinm2 = len(m2)
    if ncolm1 == nlinm2:
        return True
    else:
        return False


# -*- coding: utf-8 -*-

'''
Matrizes multiplicáveis
Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao
número de linhas da segunda.
Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como
parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e
False caso contrário.

Exemplos:

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) => False

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) => True

'''


