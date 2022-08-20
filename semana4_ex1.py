# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:16:23 2021

Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros
como parâmetro e devolve o booleano True se a lista estiver ordenada e False
se a lista não estiver ordenada.

@author: Raphael Aguiar
"""

def ordenada(lista):
    for i in range(len(lista)):
        for j in range (i + 1, len(lista)):
            if lista[i] > lista[j]:
                return False
    return True
