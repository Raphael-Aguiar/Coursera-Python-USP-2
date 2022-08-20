# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:11:32 2021

@author: Raphael Aguiar
"""

def sao_multiplicaveis(m1, m2):
    ncolm1 = len(m1[0])
    nlinm2 = len(m2)
    if ncolm1 == nlinm2:
        return True
    else:
        return False

def multiplica_matrizes (mat1, mat2):
    prova = sao_multiplicaveis(mat1, mat2)
    if prova == False:
        aviso = "As matrizes não são multiplicáveis"
        return aviso

    lin_mat3 = len(mat1)
    col_mat3 = len(mat2[0])
    mat3 = [[0] * col_mat3 for _ in range(lin_mat3)]
    cont_lin = 0
    cont_col = 0
    while cont_lin < lin_mat3:
        while cont_col < col_mat3:
            temp = mat1[cont_lin][cont_col] * mat2[cont_lin][cont_col] + mat1[cont_lin][cont_col+1] * mat2[cont_lin+1][cont_col]
            mat3[cont_lin][cont_col] = temp


    indicador_mat1 = 0
    indicador_mat2 = 0



            cont_col += 1
        cont_col = 0
        cont_lin += 1
    return mat3





mat1 = [[3,2],[5,-1]]
mat2 = [[6,4,-2],[0,7,1]]
mat3 = multiplica_matrizes (mat1, mat2)
print(mat3)






