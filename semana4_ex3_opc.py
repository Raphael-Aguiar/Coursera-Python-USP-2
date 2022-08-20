# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:50:13 2021

Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n
e devolve uma lista contendo n números inteiros aleatórios.

@author: Raphael Aguiar
"""

def lista_grande(n):
    import random
    lista = []
    for i in range(n):
       random_number = random.randint(1, 10000)
       lista.append(random_number)
    return lista
