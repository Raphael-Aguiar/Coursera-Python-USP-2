# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:19:01 2021

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz
que represente sua soma caso as matrizes tenham dimensões iguais.
Caso contrário, a função deve devolver False.

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)
=> [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)
=> False


@author: Raphael Aguiar
"""

def tem_mesmo_len(m1, m2):
    if len(m1) == len(m2):
        return True
    else:
        return False

def elementos_com_tamanhos_diferentes(m1, m2):
    resultado = True
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            resultado = False
            return False
        else:
            resultado = True
    return resultado


def soma_matrizes(m1, m2):
    matriz_temporária = []
    matriz_resultante = []
    #Checagem
    if tem_mesmo_len(m1, m2) == False:
        return False
    if elementos_com_tamanhos_diferentes(m1, m2) == False:
        return False
    #Cálculo
    i = 0
    j = 0
    while i < len(m1):
        while j < len(m1[0]):
            matriz_temporária.append(m1[i][j] + m2[i][j])
            j = j + 1
        i = i + 1 
        j = 0   
        matriz_resultante.append(matriz_temporária)
        matriz_temporária = []
    return matriz_resultante

'''
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1, m2))

'''
