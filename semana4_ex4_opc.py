# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 23:06:13 2021

Ordenação com selection sort
Implemente a função ordena(lista), que recebe uma lista com números inteiros
como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize
o algoritmo selection sort.

@author: Raphael Aguiar
"""

def ordena(lista):

    for i in range(len(lista) - 1):
        posicao_do_minimo = i

        for j in range (i + 1, len(lista)):
            if lista[posicao_do_minimo] > lista[j]:
                posicao_do_minimo = j

        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    return lista