# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:32:41 2021

Busca sequencial
Implemente a função busca(lista, elemento), que busca um determinado elemento
em uma lista e devolve o índice correspondente à posição do elemento
encontrado. Utilize o algoritmo de busca sequencial. Nos casos em que o
elemento buscado não existir na lista, a função deve devolver o booleano False.

Ex:

busca(['a', 'e', 'i'], 'e')
# deve devolver => 1

busca([12, 13, 14], 15)
# deve devolver => False

@author: Raphael Aguiar
"""

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False